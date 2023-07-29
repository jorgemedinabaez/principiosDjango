
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # aquí podemos modificar la ruta de acceso, del panel de adminitración:
    path('administrador/', admin.site.urls),
    path('', include('primeraapp.urls')),
]
