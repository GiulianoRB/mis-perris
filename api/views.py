from .serializers import PerroSerializers, AdoptadorSerializers
from perrisapp.models import Perro, Adoptador
from rest_framework import viewsets

# Create your views here.

#API

class PerroListarViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializers

class AdoptadorListarViewSet(viewsets.ModelViewSet):
    queryset = Adoptador.objects.all()
    serializer_class = AdoptadorSerializers