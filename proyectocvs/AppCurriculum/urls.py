from django.urls import path
from AppCurriculum import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('experiencia',views.experiencia,name="Experiencia"),
    path('educacion',views.estudio,name="Educacion"),
    path('idiomas',views.idiomas,name="Idiomas"),
    path('idiomas/',views.idiomas,name="Skills"),
    path('pefil',views.datos_usuario,name="Perfil"),
    path('skills',views.skills,name="Skills"),
    path('skills/',views.skills,name="Skills"),
]
