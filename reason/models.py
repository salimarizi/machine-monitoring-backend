# from django.db import models
from djongo import models

# Create your models here.
class Reason(models.Model):
    class Meta:
        db_table = 'reasons'
    id = models.ObjectIdField()
    machine_name = models.CharField(max_length=255)
    reason = models.CharField(max_length=30)