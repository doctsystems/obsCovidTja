from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Paciente

# Create your views here.
class Dashboard(LoginRequiredMixin, TemplateView):
	template_name = "dashboard/home.html"
	login_url = "core:login"

class PacienteListView(LoginRequiredMixin, ListView):
	model=Paciente
	template_name="dashboard/paciente_list.html"
	context_object_name="obj"
	login_url="core:login"
