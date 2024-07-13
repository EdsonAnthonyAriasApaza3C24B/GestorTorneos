from django.db import models
from django.utils import timezone

class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='archivos/')
    fecha_subida = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class TribunalDeJusticia(models.Model):
    miembros = models.TextField()
    funciones = models.TextField()
    resoluciones = models.TextField()

    def __str__(self):
        return f"Tribunal de Justicia {self.id}"
    class Meta:
        verbose_name = "Tribunal de justicia"
        verbose_name_plural = "Tribunal de justicia"

class ConsejoDirectivo(models.Model):
    presidente = models.CharField(max_length=100)
    secretario = models.CharField(max_length=100)
    tesorero = models.CharField(max_length=100)
    otros_miembros = models.TextField()
    funciones = models.TextField()

    def __str__(self):
        return self.presidente

    class Meta:
        verbose_name = "Consejo directivo"
        verbose_name_plural = "Consejo directivo"

class CoordinadorDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    funciones = models.TextField()
    informe_final = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Coordinador deportivo"
        verbose_name_plural = "Coordinador deportivo"


class Promocion(models.Model):
    CATEGORIAS_CHOICES = [
        ('ORO-SUPER MASTER', 'Oro-Super Master'),
        ('MASTER', 'Master'),
        ('SUPER SENIORS', 'Super Seniors'),
        ('SENIORS', 'Seniors'),
        ('MAYORES', 'Mayores'),
        ('CADETES', 'Cadetes'),
        ('MENORES', 'Menores'),
        ('JUNIOR', 'Junior'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_CHOICES)
    cuota_inscripcion = models.DecimalField(max_digits=10, decimal_places=2)
    jugadores = models.ManyToManyField('Jugador', related_name='promociones')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Promoción"
        verbose_name_plural = "Promoción"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugador"


class Disciplina(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    puntos = models.IntegerField()

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplina"

class TablaDePosiciones(models.Model):
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    puntos = models.IntegerField()

    def __str__(self):
        return f"{self.promocion.nombre} - {self.disciplina.nombre}"
    class Meta:
        verbose_name = "Tabla de posiciones"
        verbose_name_plural = "Tabla de posiciones"

class ExCadete(models.Model):
    nombre = models.CharField(max_length=100)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    carnet = models.CharField(max_length=100)
    historial_sanciones = models.TextField()

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Ex cadete"
        verbose_name_plural = "Ex cadete"

class EventoDeportivo(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    resultados = models.TextField()

    def __str__(self):
        return f"{self.disciplina.nombre} - {self.fecha}"
    class Meta:
        verbose_name = "Evento deportivo"
        verbose_name_plural = "Evento deportivo"

class Participacion(models.Model):
    ex_cadete = models.ForeignKey(ExCadete, on_delete=models.CASCADE)
    evento_deportivo = models.ForeignKey(EventoDeportivo, on_delete=models.CASCADE)
    resultado = models.TextField()

    def __str__(self):
        return f"{self.ex_cadete.nombre} - {self.evento_deportivo.disciplina.nombre}"
    class Meta:
        verbose_name = "Participación"
        verbose_name_plural = "Participación"

class Deportes(models.Model):
    deporte = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.deporte
    class Meta:
        verbose_name = "Deportes"
        verbose_name_plural = "Deportes"

class Resultado(models.Model):
    deporte = models.ForeignKey(Deportes, on_delete=models.CASCADE)
    evento = models.CharField(max_length=100)
    fecha = models.DateField()
    resultado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.evento} - {self.deporte.deporte}"
    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultado"
