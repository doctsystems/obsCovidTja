from django.urls import path
from .views import Dashboard, PacienteListView

urlpatterns=[
    path('', Dashboard.as_view(), name='dash'),
]

# URLConf para operaciones CRUD de Pacientes
urlpatterns+=[
	path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
]