from django.contrib import admin

from .models import Autor, Book

# Register your models here.
admin.site.site_header = 'Curso Django 0031'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Administrador de Django'

class AutorAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','title')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('created','name')

    def actualizar_nombre(request,queryset):
        queryset.update() 

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Autor,AutorAdmin)
admin.site.register(Book,BookAdmin)