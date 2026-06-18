from django.shortcuts import render, get_object_or_404
from medicos.models import Medicos


def home(request):
    return render(request, "medicos/index.html")


def mostrar_medicos(request):
    lista_medicos = Medicos.objects.all()
    contexto = {
        "lista_medicos": lista_medicos
    }
    
    return render(request, "medicos/lista_medicos.html", contexto)


def ver_medico(request, code):
    medico = get_object_or_404(Medicos, code=code)
    context = {
        "medico": medico
    }
    
    return render(request, "medicos/ver_medico.html", context)
