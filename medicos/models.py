from django.db import models
import uuid


def generar_code():
    return uuid.uuid4().hex # glhauh-gljhaljf-lhgfalsfh-ahkafj

class Medicos(models.Model):
    ESPECIALIDADES = (
        ("Rama del corazon", "Cardiologo"), # (Descripcion, Valor)
        ("Rama de los huevos","Traumatologo"),
        ("Rama del cerebro", "Neurologo")
    )
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_alta = models.DateField(auto_now_add=True)
    especialidad = models.CharField(choices=ESPECIALIDADES, max_length=50)
    code = models.CharField(
        max_length=32,
        unique=True,
        default=generar_code
    )
    dni = models.CharField(max_length=12)
    nro_medico = models.IntegerField(null=True, default=None)

    def __str__(self):
        return f"Nombre: {self.nombre} - Especialidad: {self.especialidad} - DNI:{self.dni}"
