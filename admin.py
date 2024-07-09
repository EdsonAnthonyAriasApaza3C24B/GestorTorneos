from django.contrib import admin
from .models import Deportes, Resultado

#Resgistro de los modelos Deportes y Resultado en el sitio de Administración
admin.site.register(Deportes)
admin.site.register(Resultado)
