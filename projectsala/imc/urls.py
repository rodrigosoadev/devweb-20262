from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="index"),
    path("calcular/<int:altura>/<int:peso>/", views.calcular_imc,
name="cacular_imc" ),
]
