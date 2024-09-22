from django.urls import path
from TerceraPreentrega.views import *

urlpatterns = [
    
    path('', inicio,name="Inicio"),
    path('Store', Tienda,name="Store"),
    path('Login', Formulariocuenta,name="Login"),

]
