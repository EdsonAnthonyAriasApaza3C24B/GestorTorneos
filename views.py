from django.shortcuts import render
from rest_framework import viewsets
from .models import Deportes, Resultado
from .serializers import DeporteSerializer, ResultadoSerializer

class DeporteViewSet(viewsets.ModelViewSet):
    queryset = Deportes.objects.all()
    serializer_class = DeporteSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer