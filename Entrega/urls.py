from django.urls import path
from TerceraPreentrega.views import *

urlpatterns = [
    
    path('', inicio,name="Inicio"),
    path('Store', Tienda,name="Store"),
    path('Login', Inicio_sesion,name="Login"),
    path('Register', Registro,name="Register"),

]
