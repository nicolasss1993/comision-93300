from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView
)
from pacientes.models import Pacientes


class PacientesListView(ListView):
    model = Pacientes
    template_name = "pacientes/listar_pacientes.html"
    context_object_name = "lista_pacientes"
    
    def get_queryset(self):
        lista_medicos = super().get_queryset() # QuerySetPacientes
        nombre = self.request.GET.get("nombre")
        
        if nombre is not None:
            lista_medicos = lista_medicos.filter(nombre__icontains=nombre)
        return lista_medicos

class PacientesCreateView(CreateView):
    model = Pacientes
    fields = ["nombre", "apellido", "dni", "telefono"]
    template_name = "pacientes/crear_pacientes.html"
    
    def get_success_url(self):
        return reverse_lazy(
            "detalle_paciente",
            kwargs={"code": self.object.code}
        )

class PacientesDetailView(DetailView):
    model = Pacientes
    template_name = "pacientes/detalle_pacientes.html"
    context_object_name = "paciente"
    slug_field = "code"
    slug_url_kwarg = "code"
    

class PacienteUpdateView(UpdateView):
    model = Pacientes
    fields = ("nombre", "apellido", "dni", "telefono")
    template_name = "pacientes/pacientes_form.html"
    slug_field = "code"
    slug_url_kwarg = "code"
    
    def get_success_url(self):
        return reverse_lazy(
            "detalle_paciente",
            kwargs={"code": self.object.code}
        )

class PacienteDeleteView(DeleteView):
    model = Pacientes
    template_name = "pacientes/paciente_consultar_eliminar.html"
    slug_field = "code"
    slug_url_kwarg = "code"
    success_url = reverse_lazy("listar_pacientes")
