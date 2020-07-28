from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class ClaseModelo(models.Model):
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	usuario_creacion = UserForeignKey(auto_user_add=True, related_name='+')
	usuario_modificacion = UserForeignKey(auto_user=True, related_name='+')

	class Meta:
		abstract=True
