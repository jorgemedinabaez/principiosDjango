
# from django.contrib import admin

from django.urls import path

from .views import (
    IndexPageReview,
    obtener_fecha,
    menu_view,
    mostrar,
    prueba,
    get_name,
    gracias_view,
    datosform_view,
    autorform_view,
    register_view,
    login_view,
    logout_view,
    authors_view
    )

urlpatterns = [
    path('',IndexPageReview.as_view(),name='index'),
    path('fecha/<str:name>/<int:foto>/',obtener_fecha,name='fecha'),
    path('menu/', menu_view,name='menu'),
    path('mostrar/',mostrar,name='mostrar'),
    path('name/',get_name,name='get_name'),
    path('Thanks/',gracias_view,name='gracias'),
    path('datosform/',datosform_view,name='datosform'),
    path('autorform/',autorform_view,name='autorform'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('authors/',authors_view,name='authors'),
    
    # y la siguiente es una ruta de prueba para probar cosas:
    path('prueba/',prueba,name='prueba'),
]