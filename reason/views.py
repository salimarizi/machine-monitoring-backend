# from django.shortcuts import render
from .models import Reason
from .serializers import ReasonSerializer
from rest_framework import viewsets

# Create your views here.
class ReasonViewsset(viewsets.ModelViewSet):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer