from django.urls import path
from AppCurriculum import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('experiencia',views.experiencia,name="Experiencia"),
    path('educacion',views.estudio,name="Educacion"),
]