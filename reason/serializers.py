from .models import Reason
from rest_framework import serializers

class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = ['id', 'machine_name', 'reason']