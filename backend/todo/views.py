from django.shortcuts import render
from rest_framework import viewsets
from .serializers import todoSerializer
from .models import todo

# Create your views here.

class todoView(viewsets.ModelViewSet):
    serializer_class = todoSerializer
    queryset = todo.objects.all()

