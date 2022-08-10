# from django.db import models
from djongo import models
from action.models import Action
from reason.models import Reason


# Create your models here.
class Anomaly(models.Model):
    class Meta:
        db_table = 'anomalies'

    _id = models.ObjectIdField(db_column='_id')
    action = models.EmbeddedField(
        model_container=Action,
        default=None, null=True
    )
    reason = models.EmbeddedField(
        model_container=Reason,
        default=None, null=True
    )
    timestamp = models.DateTimeField()
    machine = models.CharField(max_length=255)
    anomaly = models.CharField(max_length=10)
    sensor = models.IntegerField()
    sound_clip = models.CharField(max_length=255)
    wave = models.CharField(max_length=255)
    spectogram = models.CharField(max_length=255)
    comments = models.TextField()