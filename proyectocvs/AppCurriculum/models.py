from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField

    def __str__(self):
        return self.user.username   

class DataUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class ExperienciaLaboral(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='experiencias_laborales')
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f'{self.cargo} en {self.empresa}'

class Educacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='estudios')
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField(null=True, blank=True)  # Puede ser nulo si aún está estudiando

    def __str__(self):
        return f'{self.titulo} en {self.institucion}'

class Idiomas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='idiomas')
    idioma = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20)  # Puede ser un campo de selección (Básico, Intermedio, Avanzado, etc.)

    def __str__(self):
        return f'{self.idioma} - Nivel: {self.nivel}'
