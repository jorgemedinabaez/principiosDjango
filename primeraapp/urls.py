
# from django.contrib import admin

from django.urls import path

from .views import IndexPageReview,obtener_fecha,menu_view,mostrar

urlpatterns = [
    path('',IndexPageReview.as_view(),name='index'),
    path('fecha/<str:name>/<int:foto>/',obtener_fecha,name='fecha'),
    path('menu/', menu_view,name='menu'),
    path('mostrar/',mostrar,name='mostrar'),
]