# from django.shortcuts import render
from .models import Action
from .serializers import ActionSerializer
from rest_framework import viewsets

# Create your views here.
class ActionViewsset(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer