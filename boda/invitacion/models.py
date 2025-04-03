from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    direccion = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre