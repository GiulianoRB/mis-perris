from rest_framework import serializers
from perrisapp.models import Perro, Adoptador


class PerroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'color','edad_estimada']

class AdoptadorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adoptador
        fields = ['nombre_completo','ap_paterno','ap_materno','email', 'telefono', 'fecha_nacimiento']