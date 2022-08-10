from .models import Anomaly
from rest_framework import serializers

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = [
            'id',
            'action',
            'timestamp',
            'machine',
            'anomaly',
            'sensor',
            'sound_clip'
        ]