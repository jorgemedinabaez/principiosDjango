from django import forms
from .models import Autor


class NameForm(forms.Form):
    your_name = forms.CharField(label='Tu nombre:',max_length=100)


class InputForm(forms.Form):
    nombres = forms.CharField(max_length=200)
    apellidos = forms.CharField(max_length=200)
    prioridad = forms.IntegerField(widget=forms.TextInput,min_value=1,max_value=3)
    habilitado = forms.BooleanField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    contrasena = forms.CharField(widget=forms.PasswordInput())

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'