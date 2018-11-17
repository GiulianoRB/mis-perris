from django import forms
from . import models

class AdoptarPerro(forms.ModelForm):
    class Meta:
        model = models.Adoptador
        fields = ['nombre_completo','rut','direccion','telefono','email','genero','fecha_nacimiento','comentario']