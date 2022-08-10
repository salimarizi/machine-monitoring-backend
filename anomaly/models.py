# from django.db import models
from djongo import models
from action.models import Action

# Create your models here.
class Anomaly(models.Model):
    class Meta:
        db_table = 'anomalies'
    id = models.ObjectIdField()
    action = models.EmbeddedField(
        model_container=Action
    )
    timestamp = models.DateTimeField()
    machine = models.CharField(max_length=255)
    anomaly = models.CharField(max_length=10)
    sensor = models.IntegerField()
    sound_clip = models.CharField(max_length=255)