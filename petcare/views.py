from django.shortcuts import render
from rest_framework import viewsets
from .models import Tutor, Mascota, Veterinario, CitaMedica, FichaMedica, RecordatorioPreventivo
from .serializers import (
    TutorSerializer, MascotaSerializer, VeterinarioSerializer,
    CitaMedicaSerializer, FichaMedicaSerializer, RecordatorioPreventivoSerializer
)

# Vista para cargar la página web HTML
def index_view(request):
    return render(request, 'petcare/index.html')

# ViewSets para la API REST
class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class CitaMedicaViewSet(viewsets.ModelViewSet):
    queryset = CitaMedica.objects.all()
    serializer_class = CitaMedicaSerializer

class FichaMedicaViewSet(viewsets.ModelViewSet):
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer

class RecordatorioPreventivoViewSet(viewsets.ModelViewSet):
    queryset = RecordatorioPreventivo.objects.all()
    serializer_class = RecordatorioPreventivoSerializer