from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index2(request): 
    return  HttpResponse("<h1> Olá Rodrigo")

def rodrigo(request):
    return HttpResponse("Olá Rodrigo")