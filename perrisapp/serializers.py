from .models import Perro
from rest_framework import serializers


#API

class PerroSerializado(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'color','edad_estimada']