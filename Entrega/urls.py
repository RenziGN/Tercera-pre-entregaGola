from django.urls import path
from TerceraPreentrega.views import *

urlpatterns = [
    
    path('', inicio,name="Inicio"),
    path('stock', Stock,name="stock"),
    path('register', Registro,name="Register"),
    path('ventas', Ventas,name="Ventas"),

]
