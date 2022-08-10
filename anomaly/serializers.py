from action.models import Action
from .models import Anomaly
from action.models import Action
from reason.models import Reason
from rest_framework import serializers

class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = ['machine_name', 'reason']

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['name']
    
class AnomalySerializer(serializers.ModelSerializer):
    action = ActionSerializer(many=False, read_only=True)
    reason = ReasonSerializer(many=False, read_only=True)

    class Meta:
        model = Anomaly
        fields = [
            '_id',
            'action',
            'reason',
            'timestamp',
            'machine',
            'anomaly',
            'sensor',
            'sound_clip',
            'comments',
            'wave',
            'spectogram'
        ]