from django.db import models

class Deportes(models.Model):
    deporte = models.CharField(max_length=100) #nombre del deporte
    logo = models.ImageField(upload_to='logos/') #logo del deporte/equipo

    def __str__(self):
        return self.deporte
    
class Resultado(models.Model):
    deporte = models.ForeignKey(Deportes, on_delete=models.CASCADE) #clave externa del modelo Deportes
    evento = models.CharField(max_length=100) #nombre del evento
    fecha = models.DateField() #Día del evento
    resultado = models.CharField(max_length=100) #Resultado del evento

    def __str__(self):
        return f"{self.evento} - {self.deporte.deporte}"
    
