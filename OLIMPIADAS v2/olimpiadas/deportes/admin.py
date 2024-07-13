from django.contrib import admin
from .models import (
    ConsejoDirectivo, CoordinadorDeportivo, Deportes, Disciplina,
    EventoDeportivo, ExCadete, Jugador, Participacion, Promocion,
    Resultado, TablaDePosiciones, TribunalDeJusticia
)

# Registro de modelos en el sitio de administración
admin.site.register(Deportes)
admin.site.register(Resultado)
admin.site.register(TribunalDeJusticia)
admin.site.register(ConsejoDirectivo)
admin.site.register(CoordinadorDeportivo)
admin.site.register(Jugador)
admin.site.register(Disciplina)
admin.site.register(TablaDePosiciones)
admin.site.register(ExCadete)
admin.site.register(EventoDeportivo)
admin.site.register(Participacion)

@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    filter_horizontal = ('jugadores',)  # Permite una interfaz más amigable para seleccionar jugadores

