from django.urls import path
from medicos.views import *

urlpatterns = [
    path("", home, name="home"),
    path("medicos/", mostrar_medicos, name="listar_medicos"),
    path("ver_medico/<str:code>", ver_medico, name="ver_medico"),
    path("crear_medico/", crear_medico, name="crear_medico"),
    path("medico/actualizar/<str:code>", editar_medico, name="editar_medico"),
    path("medicos/eliminar/<str:code>", eliminar_medico, name="eliminar_medico"),
    path("medicos/consulta-eliminar/<str:code>", consulta_eliminar_medico, name="consulta_eliminar_medico"),
]