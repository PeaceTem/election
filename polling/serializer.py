from rest_framework import serializers
from .models import ward

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ward
        fields = ['id', 'ward_id', 'ward_name']
        depth = 1

