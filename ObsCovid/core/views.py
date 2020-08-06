from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
	template_name = "core/index.html"

class SintomasPageView(TemplateView):
	template_name = "core/sintomas.html"

class PrevencionPageView(TemplateView):
	template_name = "core/prevencion.html"

class ContactoPageView(TemplateView):
	template_name = "core/contacto.html"