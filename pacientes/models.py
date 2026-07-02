from django.db import models
from medicos.models import generar_code
# Create your models here.

class Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=12, unique=True)
    code = models.CharField(
        max_length=32,
        unique=True,
        default=generar_code
    )
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Paciente: {self.nombre}, {self.apellido}. DNI: {self.dni}"
