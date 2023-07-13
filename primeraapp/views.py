from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime


class Persona:
    def __init__(self,nombre,apellido,login):
        self.nombre = nombre
        self.apellido = apellido
        self.login = login

class IndexPageReview(TemplateView):
    template_name = 'index.html'

def index(request):
    return HttpResponse("Bienvenido a mi página, Hola Mundo.")

def obtener_fecha(request,name,foto):
    fecha_actual = datetime.datetime.now()
    context = {
        'fecha':fecha_actual,'name':name,
        'frutas':['manzana','pera','durazno'],
        'foto':foto,
    }
    return render(request,'fecha.html',context)

def menu_view(request):
    template_name = 'menu.html'
    return render(request,template_name)

def mostrar(request):
    persona = Persona('Juan','Pérex',True)
    items = ['Primero','Segundo','Tercero','Cuarto']
    context = {'nombre':persona.nombre,'apellido':persona.apellido,'login':persona.login,'items':items}
    return render(request,'seguro.html',context)