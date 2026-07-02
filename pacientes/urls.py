from django.urls import path
from pacientes.views import *

urlpatterns = [
    path("pacientes/listar", PacientesListView.as_view(), name="listar_pacientes"),
    path("pacientes/crear", PacientesCreateView.as_view(), name="crear_paciente"),
    path("editar/<str:code>", PacienteUpdateView.as_view(), name="update_pacientes"),
    path("eliminar/<str:code>", PacienteDeleteView.as_view(), name="eliminar_paciente"),
    path("detalle/<str:code>", PacientesDetailView.as_view(), name="detalle_paciente"),
]