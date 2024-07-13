from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from django.views import View
from django.views.generic import ListView, DetailView
from .models import (
    TribunalDeJusticia, ConsejoDirectivo, CoordinadorDeportivo, Promocion,
    Disciplina, TablaDePosiciones, ExCadete, EventoDeportivo, Participacion,
    Deportes, Resultado
)
from .forms import ArchivoForm
from .serializers import (
    TribunalDeJusticiaSerializer, ConsejoDirectivoSerializer, CoordinadorDeportivoSerializer,
    PromocionSerializer, DisciplinaSerializer, TablaDePosicionesSerializer, ExCadeteSerializer,
    EventoDeportivoSerializer, ParticipacionSerializer, DeportesSerializer, ResultadoSerializer
)

class TribunalDeJusticiaViewSet(viewsets.ModelViewSet):
    queryset = TribunalDeJusticia.objects.all()
    serializer_class = TribunalDeJusticiaSerializer

class ConsejoDirectivoViewSet(viewsets.ModelViewSet):
    queryset = ConsejoDirectivo.objects.all()
    serializer_class = ConsejoDirectivoSerializer

class CoordinadorDeportivoViewSet(viewsets.ModelViewSet):
    queryset = CoordinadorDeportivo.objects.all()
    serializer_class = CoordinadorDeportivoSerializer

class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class TablaDePosicionesViewSet(viewsets.ModelViewSet):
    queryset = TablaDePosiciones.objects.all()
    serializer_class = TablaDePosicionesSerializer

class ExCadeteViewSet(viewsets.ModelViewSet):
    queryset = ExCadete.objects.all()
    serializer_class = ExCadeteSerializer

class EventoDeportivoViewSet(viewsets.ModelViewSet):
    queryset = EventoDeportivo.objects.all()
    serializer_class = EventoDeportivoSerializer

class ParticipacionViewSet(viewsets.ModelViewSet):
    queryset = Participacion.objects.all()
    serializer_class = ParticipacionSerializer

class DeportesViewSet(viewsets.ModelViewSet):
    queryset = Deportes.objects.all()
    serializer_class = DeportesSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

class TribunalDeJusticiaListView(ListView):
    model = TribunalDeJusticia
    template_name = 'deportes/tribunal_list.html'

class TribunalDeJusticiaDetailView(View):
    template_name = 'deportes/tribunal_detail.html'

    def get(self, request, pk):
        tribunal = get_object_or_404(TribunalDeJusticia, pk=pk)
        archivo_form = ArchivoForm()
        context = {
            'tribunal': tribunal,
            'archivo_form': archivo_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        tribunal = get_object_or_404(TribunalDeJusticia, pk=pk)
        archivo_form = ArchivoForm(request.POST, request.FILES)
        if archivo_form.is_valid():
            nuevo_archivo = archivo_form.save(commit=False)
            nuevo_archivo.tribunal = tribunal
            nuevo_archivo.save()
            # Aquí puedes agregar lógica adicional después de guardar el archivo
            return redirect('tribunal_detail', pk=pk)
        context = {
            'tribunal': tribunal,
            'archivo_form': archivo_form,
        }
        return render(request, self.template_name, context)

class ConsejoDirectivoListView(ListView):
    model = ConsejoDirectivo
    template_name = 'deportes/consejo_list.html'

class ConsejoDirectivoDetailView(DetailView):
    model = ConsejoDirectivo
    template_name = 'deportes/consejo_detail.html'

class CoordinadorDeportivoListView(ListView):
    model = CoordinadorDeportivo
    template_name = 'coordinador_list.html'

class CoordinadorDeportivoDetailView(DetailView):
    model = CoordinadorDeportivo
    template_name = 'coordinador_detail.html'

class PromocionListView(ListView):
    model = Promocion
    template_name = 'deportes/promocion_list.html'

class PromocionDetailView(DetailView):
    model = Promocion
    template_name = 'deportes/promocion_detail.html'

class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'disciplina_list.html'

class DisciplinaDetailView(DetailView):
    model = Disciplina
    template_name = 'disciplina_detail.html'

class TablaDePosicionesListView(ListView):
    model = TablaDePosiciones
    template_name = 'deportes/tabla_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tabla_de_posiciones_list'] = self.object_list
        return context

class TablaDePosicionesDetailView(DetailView):
    model = TablaDePosiciones
    template_name = 'deportes/tabla_detail.html'

class ExCadeteListView(ListView):
    model = ExCadete
    template_name = 'excadete_list.html'

class ExCadeteDetailView(DetailView):
    model = ExCadete
    template_name = 'excadete_detail.html'

class EventoDeportivoListView(ListView):
    model = EventoDeportivo
    template_name = 'deportes/evento_list.html'

class EventoDeportivoDetailView(DetailView):
    model = EventoDeportivo
    template_name = 'deportes/evento_detail.html'

class ParticipacionListView(ListView):
    model = Participacion
    template_name = 'participacion_list.html'

class ParticipacionDetailView(DetailView):
    model = Participacion
    template_name = 'participacion_detail.html'

class DeportesListView(ListView):
    model = Deportes
    template_name = 'deportes_list.html'

class DeportesDetailView(DetailView):
    model = Deportes
    template_name = 'deportes_detail.html'

class ResultadoListView(ListView):
    model = Resultado
    template_name = 'resultado_list.html'

class ResultadoDetailView(DetailView):
    model = Resultado
    template_name = 'resultado_detail.html'
