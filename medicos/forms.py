from django import forms
from medicos.models import Medicos



class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ("nombre", "apellido", "especialidad", "dni", "nro_medico")
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el nombre"
            }),
            "apellido": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el apellido"
            }),
            "especialidad": forms.Select(attrs={
                "class": "form-select"
            }),
            "dni": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el DNI"
            }),
            "nro_medico": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el número de matrícula"
            }),
        }


class MedicosUpdateForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ("nombre", "apellido", "dni")
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el nombre"
            }),
            "apellido": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el apellido"
            }),
            "dni": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el DNI"
            })
        }
