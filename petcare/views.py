from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .models import Tutor, Mascota, Veterinario, CitaMedica, FichaMedica, RecordatorioPreventivo
from .serializers import (
    TutorSerializer, MascotaSerializer, VeterinarioSerializer,
    CitaMedicaSerializer, FichaMedicaSerializer, RecordatorioPreventivoSerializer
)

# --- VISTAS DE AUTENTICACIÓN Y NAVEGACIÓN ---

@login_required(login_url='/login/')
def index_view(request):
    return render(request, 'petcare/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            
    return render(request, 'petcare/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

# --- VIEWSETS DE LA API REST ---

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