from django.urls import path
from . import views
urlpatterns = [
    path("", views.index,name='index'),
    path("rodrigo/",views.rodrigo,name='rodrigo'),
    path("tabuada2/",views.tabuada2,name='tabuada2'),
    path("calcular/",views.calcular_imc,name='calcular_imc')
]