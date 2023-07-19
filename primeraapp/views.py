from django.shortcuts import render
from tokenize import PseudoExtras
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import NameForm, InputForm,AutorForm,UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
# importaremos decoradores:
from django.contrib.auth.decorators import login_required,permission_required
# importamos el modelo autor para los permisos:
from .models import Autor
# gestionar permisos:
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# importamos el mixin:
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin        
import datetime


class Persona:
    def __init__(self,nombre,apellido,login):
        self.nombre = nombre
        self.apellido = apellido
        self.login = login

class IndexPageReview(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'index.html'
    permission_required = 'primeraapp.es_miembro_1'

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

@login_required(login_url='/login/')
def menu_view(request):
    template_name = 'menu.html'
    return render(request,template_name)

@login_required(login_url='/login/')
def mostrar(request):
    persona = Persona('Juan','Pérex',True)
    items = ['Primero','Segundo','Tercero','Cuarto']
    context = {'nombre':persona.nombre,'apellido':persona.apellido,'login':persona.login,'items':items}
    return render(request,'seguro.html',context)

@permission_required(login_url='/login/')
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

def autor_view(request):
# permitirá ver a todos los autores registrados en una tabla llamada 'autor.view'.
    pass

def autorform_view(request):
    context = {}
    form = AutorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/Thanks/')
    context['form'] = form
    return render(request,'datosform.html',context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # obtenemos el contenttype del modelo:
            content_type = ContentType.objects.get_for_model(Autor)
            # obtenemos el permiso a asignar:
            es_miembro_1 = Permission.objects.get(
                codename='es_miembro_1',
                content_type=content_type
            )
            user = form.save()
            # agregar el permiso al usuario al momento del registro:
            user.user_permissions.add(es_miembro_1)
            login(request,user)
            messages.success(request,'registrado satisfactoriamente')
        else:
            messages.error(request,'registro inválido. Algunos datos ingresados no son correctos')
        return HttpResponseRedirect('/menu')
    
    form = UserRegisterForm()
    context = {'register_form':form}
    return render(request,'registro.html',context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'iniciaste sesión como: {username}.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request,'username y/o password incorrecto')
                return HttpResponseRedirect('/login')
        else:
            messages.error(request,'username y/o password incorrecto')
            return HttpResponseRedirect('/login')

    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    messages.info(request,'Se ha cerrado sesión exitosamente.')
    return HttpResponseRedirect('/menu')