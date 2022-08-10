# from django.shortcuts import render
from .models import Anomaly
from .serializers import AnomalySerializer
from rest_framework import viewsets

# Create your views here.
class AnomalyViewsset(viewsets.ModelViewSet):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer