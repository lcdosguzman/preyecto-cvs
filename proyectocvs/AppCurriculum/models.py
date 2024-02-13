from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username   

class DataUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    telefono = models.CharField(max_length=20)
    url_twitter = models.CharField(max_length=30)
    url_facebook = models.CharField(max_length=30)
    url_github= models.CharField(max_length=30)
    url_youtube = models.CharField(max_length=30)
    url_linkedin = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class ExperienciaLaboral(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo_inicio = models.IntegerField()
    periodo_fin = models.IntegerField(null=True, blank=True) 
    description = models.CharField(max_length=1000)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cargo} en {self.empresa}'

class Educacion(models.Model):
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pais = models.CharField(max_length=50)
    periodo_inicio = models.IntegerField()
    periodo_fin = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f'{self.titulo} en {self.institucion}'

class Idiomas(models.Model):
    idioma = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20) 

    def __str__(self):
        return f'{self.idioma} - Nivel: {self.nivel}'
    
class Skills(models.Model):
    aptitud = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.aptitud}'