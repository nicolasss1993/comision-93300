from django.urls import path
from medicos.views import *

urlpatterns = [
    path("", home, name="home"),
    path("medicos/", mostrar_medicos, name="listar_medicos"),
    path("ver_medico/<str:code>", ver_medico, name="ver_medico"),
]