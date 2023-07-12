from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime

class IndexPageReview(TemplateView):
    template_name = 'index.html'

def index(request):
    return HttpResponse("Bienvenido a mi página, Hola Mundo.")

def obtener_fecha(request,name):
    fecha_actual = datetime.datetime.now()
    context = {'fecha':fecha_actual,'name':name,
    'frutas':['manzana','pera','durazno'],}
    return render(request,'fecha.html',context)

def menu_view(request):
    template_name = 'menu.html'
    return render(request,template_name)