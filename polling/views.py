from typing import Any, Dict
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, TemplateView, View
from .models import *

from django.http import JsonResponse


class PollingUnitDetailView(DetailView):
    model = polling_unit
    template_name = 'polling/polling_unit.html'
    context_object_name = 'polling_unit'
    # slug_field = 'id'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        polling_unit = context['polling_unit']
        try:
            context['lga'] = lga.objects.get(lga_id=polling_unit.lga_id)
        except:
            pass

        return context
    

class LGAView(TemplateView):
    template_name = 'polling/lga.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lgas"] = lga.objects.all()

        return context
    

def totalLgaResult(request, lga_id):
    print(lga_id)
    polling_units = polling_unit.objects.filter(lga_id=lga_id)
    print("Working")
    print(polling_units)
    polling_unit_uniqueids = []
    for pu in polling_units:
        polling_unit_uniqueids.append(pu.id)

    print(polling_unit_uniqueids)
    announced_results = announced_pu_results.objects.filter(polling_unit_uniqueid__in=polling_unit_uniqueids)
    print(announced_results)
    result = 0
    for res in announced_results:
        result += res.party_score

    return JsonResponse({'total':result})

from django.contrib import messages

class CreatePollingUnit(TemplateView):
    template_name='polling/create_polling_unit.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['lgas'] = lga.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        polling_unit_id = self.request.POST.get('polling_unit_id')
        polling_unit_number = self.request.POST.get('polling_unit_number')
        polling_unit_name = self.request.POST.get('polling_unit_name')
        polling_unit_description = self.request.POST.get('polling_unit_description')
        lat = self.request.POST.get('lat')
        long = self.request.POST.get('long')
        lga_id = self.request.POST.get('lga_id')
        ward_id = self.request.POST.get('ward_id').split('|')

        polling_unit.objects.create(polling_unit_id=polling_unit_id,
                                    polling_unit_number=polling_unit_number,
                                    polling_unit_name=polling_unit_name,
                                    polling_unit_description=polling_unit_description,
                                    lat=lat,
                                    long=long,
                                    lga_id=lga_id,
                                    ward_id=ward_id[0],
                                    uniquewardid=ward_id[1])
        messages.success(self.request, 'Polling unit registered successfully!')

        return redirect(self.request.META.get("HTTP_REFERER"))



from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import WardSerializer


@api_view(['GET'])
def getWards(request, lga_id):
    print(lga_id)
    wards = ward.objects.filter(lga_id=lga_id)
    print("Working")
    wards = WardSerializer(wards, many=True).data
    return Response(wards)

