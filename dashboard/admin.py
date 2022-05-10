from django.contrib import admin
from .models import *

from leaflet.admin import LeafletGeoAdmin

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Persona)
admin.site.register(Especialidad)
admin.site.register(Medicamento)
admin.site.register(EnfermedadBase)
admin.site.register(Entidad, LeafletGeoAdmin)
admin.site.register(Contacto)
admin.site.register(Paciente, LeafletGeoAdmin)
admin.site.register(HistoriaClinica)
admin.site.register(Sintomatologia)
admin.site.register(Tratamiento)
admin.site.register(Medico)