from django import forms

class UserFormulario(forms.Form):

    User = forms.CharField(required=True)
    Password = forms.CharField(required=True)
    Mail = forms.CharField(required=True)

class Producto(forms.Form):

    nombre = forms.CharField(required=True)
    stock = forms.CharField(required=True)
    Precio = forms.CharField(required=True)