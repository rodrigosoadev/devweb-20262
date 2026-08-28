from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request): 
    return  render(request, "index.html")

def rodrigo(request): 
    return  HttpResponse("<h1> Olá Rodrigo!!</h1>")

def calcular_imc(request,altura,peso):
    altura=altura/100.0
    peso=peso
    response='<h1>Calculo do IMC</h1>'
    response+=f'<h2>Altura: {altura} m</h2>'
    response+=f'<h2>Peso: {peso} kg</h2>'
    response+=f'<h2>IMC: {peso/(altura*altura)}</h2>'
    response+=f'<h2>Classificação: '
    if peso/(altura*altura)<18.5:
        response+='Abaixo do peso'
    elif peso/(altura*altura)<24.9:
        response+='Peso normal'
    elif peso/(altura*altura)<29.9:
        response+='Sobrepeso'
    else:
        response+='Obesidade'
    response+='</h2>'
    return HttpResponse(response)