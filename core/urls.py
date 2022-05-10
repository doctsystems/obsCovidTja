from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePageView, SintomasPageView, PrevencionPageView, ContactoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),

    path('sintomas/', SintomasPageView.as_view(), name="sintomas"),
    path('prevencion/', PrevencionPageView.as_view(), name="prevencion"),
    path('contacto/', ContactoPageView.as_view(), name="contacto"),

    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html'), name='logout'),

]