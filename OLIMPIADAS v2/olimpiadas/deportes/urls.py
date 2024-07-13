from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import (
    ConsejoDirectivoDetailView, ConsejoDirectivoListView, PromocionDetailView, PromocionListView, TribunalDeJusticiaViewSet, ConsejoDirectivoViewSet, CoordinadorDeportivoViewSet,
    PromocionViewSet, DisciplinaViewSet, TablaDePosicionesViewSet, ExCadeteViewSet,
    EventoDeportivoViewSet, ParticipacionViewSet, DeportesViewSet, ResultadoViewSet,
    TribunalDeJusticiaListView, TribunalDeJusticiaDetailView,EventoDeportivoListView, EventoDeportivoDetailView, TablaDePosicionesListView, TablaDePosicionesDetailView
)


router = DefaultRouter()
router.register(r'tribunal', TribunalDeJusticiaViewSet)
router.register(r'consejo', ConsejoDirectivoViewSet)
router.register(r'coordinador', CoordinadorDeportivoViewSet)
router.register(r'promocion', PromocionViewSet)
router.register(r'disciplina', DisciplinaViewSet)
router.register(r'tabla', TablaDePosicionesViewSet)
router.register(r'excadete', ExCadeteViewSet)
router.register(r'evento', EventoDeportivoViewSet)
router.register(r'participacion', ParticipacionViewSet)
router.register(r'deportes', DeportesViewSet)
router.register(r'resultado', ResultadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tribunall/', TribunalDeJusticiaListView.as_view(), name='tribunal_list'),
    path('tribunall/<int:pk>/', TribunalDeJusticiaDetailView.as_view(), name='tribunal_detail'),
    path('consejos/', ConsejoDirectivoListView.as_view(), name='consejo_list'),
    path('consejos/<int:pk>/', ConsejoDirectivoDetailView.as_view(), name='consejo_detail'),
    path('promocionn/', PromocionListView.as_view(), name='promocion_list'),
    path('promocionn/<int:pk>/', PromocionDetailView.as_view(), name='promocion_detail'),

    #Agregado por Niels T
    path('eventos/', EventoDeportivoListView.as_view(), name='evento_list'),
    path('eventos/<int:pk>/', EventoDeportivoDetailView.as_view(), name='evento_detail'),
    path('tablas/', TablaDePosicionesListView.as_view(), name='tabla_list'),
    path('tablas/<int:pk>/', EventoDeportivoDetailView.as_view(), name='tabla_detail'),
]

# Configuración para servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
