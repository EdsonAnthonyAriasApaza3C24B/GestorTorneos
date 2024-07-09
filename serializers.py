from rest_framework import serializers
from .models import Deportes, Resultado

class DeporteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Deportes
        fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Resultado
        fields = '__all__'