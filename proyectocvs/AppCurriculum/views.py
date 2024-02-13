from django.shortcuts import render
from django.http import HttpResponse
from AppCurriculum.models import *
from AppCurriculum.forms import *

def home(request):
    experiencias = ExperienciaLaboral.objects.all()
    estudios = Educacion.objects.all()
    idiomas = Idiomas.objects.all()
    perfil=DataUsuario.objects.latest('id')
    return render(request,"AppCurriculum/home.html",{"experiencias":experiencias,"estudios":estudios,"idiomas":idiomas,"perfil":perfil})

def experiencia(request):
    experiencias = ExperienciaLaboral.objects.all()
    if request.method == 'POST':
        miFormulario = ExperienciaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            if 'periodo_inicio'in request.POST and 'periodo_fin'in request.POST:
                informacion = miFormulario.cleaned_data
                exp = ExperienciaLaboral (cargo=informacion['cargo'],empresa=informacion['empresa'],periodo_fin=informacion['periodo_fin'],periodo_inicio=informacion['periodo_inicio'],description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = ExperienciaFormulario()
                return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente"})
            else:
                return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos No Gurdados"})
    else:
        miFormulario = ExperienciaFormulario()

    return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario})

def estudio(request):
    estudios = Educacion.objects.all()
    if request.method == 'POST':
        miFormulario = EstudioFormulario(request.POST)
        if miFormulario.is_valid():
            if 'periodo_inicio'in request.POST and 'periodo_fin'in request.POST:
                informacion = miFormulario.cleaned_data
                exp = Educacion(institucion=informacion['institucion'],titulo=informacion['titulo'],periodo_fin=informacion['periodo_fin'],periodo_inicio=informacion['periodo_inicio'],description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = EstudioFormulario()
                return render(request,"AppCurriculum/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente"})
            else:
                return render(request,"AppCurriculum/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos No Gurdados"})
    else:
        miFormulario = EstudioFormulario()

    return render(request,"AppCurriculum/educacion.html",{"estudios":estudios,"miFormulario":miFormulario})

def idiomas(request):
    idiomas = Idiomas.objects.all()
    if request.method == 'POST':
        miFormulario = IdiomaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            exp = Idiomas(idioma=informacion['idioma'],nivel=informacion['nivel'])
            exp.save()
            miFormulario = IdiomaFormulario()
            return render(request,"AppCurriculum/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente"})
    else:
        miFormulario = IdiomaFormulario()

    return render(request,"AppCurriculum/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario})

def datos_usuario(request):
    data=DataUsuario.objects.latest('id')
    if request.method == 'POST':
        miFormulario = DataUsuarioFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            exp = DataUsuarioFormulario(nombre=informacion['nombre'],apellido=informacion['apellido'],
                              bio=informacion['bio'],telefono=informacion['telefono'],url_twitter=informacion['url_twitter'],
                              url_facebook=informacion['url_facebook'],url_github=informacion['url_github'],
                              url_youtube=informacion['url_youtube'],url_linkedin=informacion['url_linkedin'])
            exp.save()
            miFormulario = DataUsuarioFormulario()
            return render(request,"AppCurriculum/perfil.html",{"data":data,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente"})
    else:
        miFormulario = DataUsuarioFormulario()

    return render(request,"AppCurriculum/perfil.html",{"info":data,"miFormulario":miFormulario})