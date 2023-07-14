from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(label='Tu nombre:',max_length=100)


class InputForm(forms.Form):
    nombres = forms.CharField(max_length=200)
    apellidos = forms.CharField(max_length=200)
    prioridad = forms.IntegerField(min_value=1,max_value=3)
    contrasena = forms.CharField(widget=forms.PasswordInput())
    