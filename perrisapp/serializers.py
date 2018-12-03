from .models import Perro, Adoptador
from rest_framework import serializers


#API

class PerroSerializado(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'color','edad_estimada']


class AdoptadorSerializado(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adoptador
        fields = ['nombre_completo','ap_paterno','ap_materno','email', 'telefono', 'fecha_nacimiento']

