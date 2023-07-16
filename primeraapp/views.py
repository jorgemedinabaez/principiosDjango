from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import NameForm, InputForm,AutorForm
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

def prueba(request):
    template_name = 'formulario.html'
    return render(request,'formulario.html')

def get_name(request):
    # si se trata de una solicitud post, debemos procesar los datos del formulario.
    if request.method == 'POST':
        print(request.POST)
    # crea una instancia de formulario y se completa con los datos de la solicitud:
        form = NameForm(request.POST)
    # ahora, comprobar si los datos son válidos:
        if form.is_valid():
    # aquí se procesan los datos en 'form.cleaned_data' según sea necesario.
    # redirigimos a continuación, a una nueva URL.
            return HttpResponseRedirect('/Thanks/')
    # si por el contrario, tenemos un métogo get o cualquier otro método, crearemos un formulario en blanco.
    else:
        form = NameForm()
        context = {'form':form}
    return render(request,'name.html',context)

def gracias_view(request):
    return HttpResponse('<h1>Datos ingresados correctamente</h1>')

def datosform_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request,'datosform.html',context)

def autorform_view(request):
    context = {}
    form = AutorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Thanks/')
    context['form'] = form
    return render(request,'datosform.html',context)