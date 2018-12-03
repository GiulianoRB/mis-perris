from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework import viewsets
from .models import Perro, Adoptador
from .serializers import PerroSerializado, AdoptadorSerializado

# Create your views here.
def index(request):
    return render(request, 'perrisapp/index.html')

@login_required(login_url = "/accounts/login/")
def formulario(request):
    form = forms.AdoptarPerro()
    return render(request, 'perrisapp/formulario.html', {'form':form})

#API

class PerroListarViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializado

class AdoptadorListarViewSet(viewsets.ModelViewSet):
    queryset = Adoptador.objects.all()
    serializer_class = AdoptadorSerializado
