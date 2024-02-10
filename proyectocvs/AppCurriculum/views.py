from django.shortcuts import render
from django.http import HttpResponse
from AppCurriculum.models import *

# Create your views here.
def home(request):
    experiencias = ExperienciaLaboral.objects.all()
    estudios = Educacion.objects.all()
    return render(request,"AppCurriculum/home.html",{"experiencias":experiencias,"estudios":estudios})

def experiencia(request):
    experiencias = ExperienciaLaboral.objects.all()
    return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias})
