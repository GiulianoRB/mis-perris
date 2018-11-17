from django.db import models
from django.utils import timezone

# Create your models here.
class Adoptador(models.Model):
    nombre_completo = models.CharField(max_length = 200)
    ap_paterno = models.CharField(max_length = 200)
    ap_materno = models.CharField(max_length = 200)
    rut = models.CharField(max_length = 12)
    direccion = models.CharField(max_length = 200)
    telefono = models.IntegerField()
    email = models.CharField(max_length = 200)
    genero = models.CharField(max_length = 1)
    fecha_nacimiento = models.DateField()
    comentario = models.TextField(null=True)
    
    def __str__(self):
        return self.nombre_completo +' '+ self.ap_paterno

class Perro(models.Model):
    adoptador = models.ForeignKey(Adoptador, on_delete=models.SET_NULL, null = True)
    nombre = models.CharField(max_length = 50)
    raza = models.CharField(max_length = 20)
    color = models.CharField(max_length = 20)
    fecha_encontrado = models.DateTimeField(default = timezone.now)
    edad_estimada = models.IntegerField()
    sitio_encontrado = models.CharField(max_length = 200)
    fecha_publicacion = models.DateTimeField(blank = True, null = True)

    def publico(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

