from django.urls import path
from .views import *

urlpatterns = [
    path('polling-unit/<int:pk>', PollingUnitDetailView.as_view(), name='polling_unit_detail'),
    path('lga/', LGAView.as_view(), name="lga"),
    path('lga_total/<int:lga_id>', totalLgaResult, name='lga_total'),
    path('wards/<int:lga_id>', getWards, name='wards'),
    path('create_polling_unit/', CreatePollingUnit.as_view(), name='create-polling-unit'),
]