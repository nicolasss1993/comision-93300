from django.contrib import admin
from medicos.models import Medicos


#admin.site.register(Medicos)
# Register your models here.

@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "especialidad")
    
    list_display_links = ("nombre",)
    
    search_fields = ("dni", "especialidad")
    
    list_filter = ("fecha_de_alta",)
    
    ordering = ("nombre", "apellido", "nro_medico")
    
    readonly_fields = ("fecha_de_alta",)
