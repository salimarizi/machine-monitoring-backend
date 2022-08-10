# from django.db import models
from djongo import models

# Create your models here.
class Action(models.Model):
    class Meta:
        db_table = 'actions'
    id = models.ObjectIdField()
    name = models.CharField(max_length=10)