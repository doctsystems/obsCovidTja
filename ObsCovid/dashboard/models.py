from django.db import models
from core.models import ClaseModelo
from django.contrib.gis.db import models

class Persona(ClaseModelo):
	nombres=models.CharField(max_length=20)
	apellidos=models.CharField(max_length=30)
	carnet=models.CharField(max_length=10)
	celular=models.IntegerField(default=0)
	direccion=models.CharField(max_length=100)
	fecha_nacimiento=models.DateField()

	OPositivo='O +'
	ONegativo='O -'
	APositivo='A +'
	ANegativo='A -'
	BPositivo='B +'
	BNegativo='B -'
	ABPositivo='AB +'
	ABNegativo='AB -'
	TIPO_SANGRE=[
		(OPositivo, 'O +'),
		(ONegativo, 'O -'),
		(APositivo, 'A +'),
		(ANegativo, 'A -'),
		(BPositivo, 'B +'),
		(BNegativo, 'B -'),
		(ABPositivo, 'AB +'),
		(ABNegativo, 'AB -'),
	]
	grupo_sanguineo=models.CharField(max_length=5, choices=TIPO_SANGRE, default=OPositivo)

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)

	def save(self):
		self.nombres=self.nombres.upper()
		self.apellidos=self.apellidos.upper()
		super(Persona, self).save()

	class Meta:
		verbose_name_plural='Personas'

	def get_absolute_url(self):
		return reverse('persona-detalle', args=[str(self.id)])

class Especialidad(ClaseModelo):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=100)
	observaciones=models.TextField(blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(Especialidad, self).save()

	class Meta():
		verbose_name_plural='Especialidades'

class Medicamento(ClaseModelo):
	nombre=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(Medicamento, self).save()

	class Meta():
		verbose_name_plural='Medicamentos'

class EnfermedadBase(ClaseModelo):
	nombre=models.CharField(max_length=20)
	descripcion=models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(EnfermedadBase, self).save()

	class Meta():
		verbose_name_plural='Enfermedades de Base'

class Sintomatologia(ClaseModelo):
	nombre=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=50)
	observaciones=models.TextField(blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(Sintomatologia, self).save()

	class Meta():
		verbose_name_plural='Sintomas'

class Departamento(ClaseModelo):
	nombre=models.CharField(max_length=10)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(Departamento, self).save()

	def get_absolute_url(self):
		return reverse('departamento-detail-view', args=[str(self.id)])

	class Meta():
		verbose_name_plural='Departamentos'

class Municipio(ClaseModelo):
	nombre=models.CharField(max_length=30)
	departamento=models.ForeignKey(Departamento, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(Municipio, self).save()

	class Meta():
		verbose_name_plural='Municipios'

class Entidad(ClaseModelo):
	nombre=models.CharField(max_length=100)
	direccion=models.CharField(max_length=100)
	telefono=models.IntegerField(default=0)
	observaciones=models.TextField(blank=True, null=True)

	ciudad=models.ForeignKey(Municipio, blank=True, null=True, on_delete=models.SET_NULL)
	ubicacion=models.PointField(srid=4326)

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(Entidad, self).save()

	class Meta():
		verbose_name_plural='Entidades'

class Contacto(ClaseModelo):
	datos_personales=models.ForeignKey(Persona, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.datos_personales.nombres, self.datos_personales.apellidos)

	class Meta():
		verbose_name_plural='Contactos'

class Paciente(ClaseModelo):
	datos_personales=models.ForeignKey(Persona, blank=True, null=True, on_delete=models.SET_NULL)
	contactos_directos=models.ManyToManyField(Contacto)
	ciudad=models.ForeignKey(Municipio, blank=True, null=True, on_delete=models.SET_NULL)
	ubicacion=models.PointField(srid=4326)

	def __str__(self):
		return '{} {}'.format(self.datos_personales.nombres, self.datos_personales.apellidos)

	class Meta():
		verbose_name_plural='Pacientes'

class Medico(ClaseModelo):
	datos_personales=models.ForeignKey(Persona, blank=True, null=True, on_delete=models.SET_NULL)
	matricula=models.CharField(max_length=20)
	especialidad=models.ForeignKey(Especialidad, blank=True, null=True, on_delete=models.SET_NULL)
	entidad_medica=models.ForeignKey(Entidad, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {} {}'.format(self.matricula, self.datos_personales.nombres,self.datos_personales.apellidos)

	class Meta():
		verbose_name_plural='Medicos'

class Usuario(ClaseModelo):
	info=models.OneToOneField(Medico, on_delete=models.CASCADE)
	nombre_usuario=models.CharField(max_length=20)
	contraseña=models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.nombre_usuario)

	class Meta():
		verbose_name_plural='Usuarios del Sistema'

class Receta(ClaseModelo):
	medicamento=models.ManyToManyField(Medicamento, help_text="Seleccione un medicamento.")
	dosificacion=models.CharField(max_length=50)
	observaciones=models.TextField(blank=True, null=True)

	def __str__(self):
		return '{} {}'.format(self.id, self.dosificacion)

	class Meta():
		verbose_name_plural='Recetas'

class HistoriaClinica(ClaseModelo):
	fecha=models.DateField()
	paciente=models.ForeignKey(Paciente, blank=True, null=True, on_delete=models.SET_NULL)
	enfermedades=models.ManyToManyField(EnfermedadBase, help_text="Seleccione una enfermedad.")
	sintomas=models.ManyToManyField(Sintomatologia, help_text="Seleccione un sintoma.")
	medico=models.ForeignKey(Medico, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.fecha, self.paciente.datos_personales.nombres)

	class Meta():
		verbose_name_plural='Historiales Medicos'

class Tratamiento(ClaseModelo):
	fecha_inicio=models.DateField()
	fecha_final=models.DateField()
	lista_medicacion=models.ForeignKey(Receta, blank=True, null=True, on_delete=models.SET_NULL)
	historial=models.ForeignKey(HistoriaClinica, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.fecha_inicio, self.fecha_final)

	class Meta():
		verbose_name_plural='Tratamientos Medicos'

