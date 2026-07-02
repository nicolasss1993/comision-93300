from django.shortcuts import render, get_object_or_404, redirect
from medicos.models import Medicos
from medicos.forms import MedicosForm, MedicosUpdateForm


def home(request):
    return render(request, "medicos/index.html")


def mostrar_medicos(request):
    nombre = request.GET.get("nombre")
    lista_medicos = Medicos.objects.all()
    if nombre is not None:
        lista_medicos = lista_medicos.filter(nombre__icontains=nombre)

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

# CRUD
# Create - Crear registros de ese Modelo
# Read - Leer informacion de ese modelo
# Update - Actualizar/editar informacion de ese modelo
# Delete - Eliminar informacion de ese modelo

# GET - Se pide informacion
# POST - Crear informacion / "editar" informacion.
# PUT - Actualizar Informacion
# Delete - Eliminar Informacion.

def crear_medico(request):
    if request.method == "POST":
        form = MedicosForm(request.POST) # .. request.POST - TRAE TODA LA INFO QUE EL USUARIO RELLENO EN EL FORMULARIO
        if form.is_valid():
            form.save()
            return redirect("listar_medicos")
    else:
        form = MedicosForm()
    
    return render(request, "medicos/crear_medico.html", { "form":form })


def editar_medico(request, code):
    medico = get_object_or_404(Medicos, code=code)
    
    if request.method == "POST":
        form = MedicosUpdateForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect("ver_medico", code=code)
    else:
        form = MedicosUpdateForm(instance=medico)
    
    return render(request, "medicos/editar_medico.html", {
        "form": form,
        "medico": medico
    })


def consulta_eliminar_medico(request, code):
    return render(request, "medicos/eliminar_medicos.html", {"code": code})


def eliminar_medico(request, code):
    medico = get_object_or_404(Medicos, code=code)
    if request.method == "POST":
        medico.delete()
        return redirect("listar_medicos")
