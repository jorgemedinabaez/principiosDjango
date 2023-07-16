# se importa la clase interna de django forms, para la creación de formularios.
from django import forms
from .models import Autor
# importar clases para el registro de usuario con el auth de django.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

# agregando para registro de usuarios:
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    # def save(self,commit=True):
    #     user = super(UserRegisterForm,self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
        