from django.shortcuts import render
from django.http import HttpResponse
from AppCurriculum.models import *
from AppCurriculum.forms import *

def home(request):
    experiencias = ExperienciaLaboral.objects.all()
    estudios = Educacion.objects.all()
    idiomas = Idiomas.objects.all()
    perfil=DataUsuario.objects.latest('id')
    skills = Skills.objects.all()
    return render(request,"AppCurriculum/home.html",{"experiencias":experiencias,"estudios":estudios,"idiomas":idiomas,"perfil":perfil,"skills":skills})

def experiencia(request):
    experiencias = ExperienciaLaboral.objects.all()
    if request.method == 'POST':
        miFormulario = ExperienciaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            if 'periodo_inicio'in request.POST:
                informacion = miFormulario.cleaned_data
                exp = ExperienciaLaboral (cargo=informacion['cargo'],empresa=informacion['empresa'],periodo_fin=informacion['periodo_fin'],periodo_inicio=informacion['periodo_inicio'],description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = ExperienciaFormulario()
                return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
            else:
                return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos No Gurdados","respSearch":""})
    else:
        miFormulario = ExperienciaFormulario()
    
    if 'text_search' in request.GET:
        search = request.GET['text_search']
        experienciaSearch = ExperienciaLaboral.objects.filter(description__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if experienciaSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"experienciaSearch":experienciaSearch,"resp":"","respSearch":respSearch})

    return render(request,"AppCurriculum/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"","respSearch":""})

def estudio(request):
    estudios = Educacion.objects.all()
    if request.method == 'POST':
        miFormulario = EstudioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            
                informacion = miFormulario.cleaned_data
                exp = Educacion(institucion=informacion['institucion'],titulo=informacion['titulo'],periodo_fin=int(informacion['periodo_fin']),periodo_inicio=int(informacion['periodo_inicio']),description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = EstudioFormulario()
                return render(request,"AppCurriculum/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
        else:
          return render(request,"AppCurriculum/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos NO guardados Correctamente","respSearch":""})
    else:
        miFormulario = EstudioFormulario()

    if 'text_search' in request.GET:
        search = request.GET['text_search']
        estudiosSearch = Educacion.objects.filter(description__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if estudiosSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"AppCurriculum/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"estudiosSearch":estudiosSearch,"resp":"","respSearch":respSearch})

    return render(request,"AppCurriculum/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"","respSearch":""})

def idiomas(request):
    idiomas = Idiomas.objects.all()
    if request.method == 'POST':
        miFormulario = IdiomaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            exp = Idiomas(idioma=informacion['idioma'],nivel=informacion['nivel'])
            exp.save()
            miFormulario = IdiomaFormulario()
            return render(request,"AppCurriculum/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
    else:
        miFormulario = IdiomaFormulario()

    if 'text_search' in request.GET:
        search = request.GET['text_search']
        idiomaSearch = Idiomas.objects.filter(idioma__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if idiomaSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"AppCurriculum/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"idiomaSearch":idiomaSearch,"resp":"","respSearch":respSearch})

    return render(request,"AppCurriculum/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"resp":"","respSearch":""})

def datos_usuario(request):
    #está asi porque por ahora solo se manejará un perfil
    data=DataUsuario.objects.latest('id')
    if request.method == 'POST':
        miFormulario = DataUsuarioFormulario(request.POST)
        print("antes")
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print("aaa")
            exp = DataUsuario.objects.get(id=1)
            exp.nombre = informacion['nombre']
            exp.apellido = informacion['apellido']
            exp.bio = informacion['bio']
            exp.telefono = informacion['telefono']
            exp.url_twitter = informacion['url_twitter']
            exp.url_facebook = informacion['url_facebook']
            exp.url_github = informacion['url_github']
            exp.url_youtube = informacion['url_youtube']
            exp.url_linkedin = informacion['url_linkedin']
            exp.save()
            miFormulario = DataUsuarioFormulario(initial={
            'nombre': informacion['nombre'],
            'apellido': informacion['apellido'],
            'bio': informacion['bio'],
            'telefono': informacion['telefono'],
            'url_twitter': informacion['url_twitter'],
            'url_facebook': informacion['url_facebook'],
            'url_github': informacion['url_github'],
            'url_youtube': informacion['url_youtube'],
            'url_linkedin': informacion['url_linkedin'],})
            data=DataUsuario.objects.latest('id')
            return render(request,"AppCurriculum/perfil.html",{"info":data,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente"})
    else:
       miFormulario = DataUsuarioFormulario(initial={
            'nombre': data.nombre,
            'apellido': data.apellido,
            'bio': data.bio,
            'telefono': data.telefono,
            'url_twitter': data.url_twitter,
            'url_facebook': data.url_facebook,
            'url_github': data.url_github,
            'url_youtube': data.url_youtube,
            'url_linkedin': data.url_linkedin,
        })

    return render(request,"AppCurriculum/perfil.html",{"info":data,"miFormulario":miFormulario})

def skills(request):
    skills = Skills.objects.all()

 #manejo del post para agregar 
    if request.method == 'POST':
        miFormulario = SkillFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            exp = Skills(aptitud=informacion['aptitud'])
            exp.save()
            miFormulario = SkillFormulario()
            return render(request,"AppCurriculum/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
        else:
            return render(request,"AppCurriculum/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":""})
    else:
        miFormulario = SkillFormulario()

#manejo de busquedas 
    if 'skill_search' in request.GET:
        search = request.GET['skill_search']
        skillsSearch = Skills.objects.filter(aptitud__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if skillsSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"AppCurriculum/skills.html",{"skills":skills,"miFormulario":miFormulario,"skillsSearch":skillsSearch,"resp":"","respSearch":respSearch})


    return render(request,"AppCurriculum/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"","respSearch":""})