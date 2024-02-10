from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"AppCurriculum/home.html")

def experiencia(request):
    return render(request,"AppCurriculum/experiencia.html")
