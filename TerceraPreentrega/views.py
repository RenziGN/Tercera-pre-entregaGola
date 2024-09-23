from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from Entrega.forms import UserFormulario
from Entrega.models import *
from django.template import Template,Context,loader

def Tienda(req):
    plantilla = loader.get_template("tienda.html")
    documento = plantilla.render()
    return HttpResponse(documento)


def inicio(req):
    plantilla = loader.get_template("Inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def Inicio_sesion(req):

    return render(req,"inicio_sesion.html",{})

def Registro(req):
    print("data",req.POST)
    if req.method == "POST":
        mi_formulario = UserFormulario(req.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            nuevo_usuario = Usuarios(User=data["User"],Password=data["Password"],Mail=data["Mail"])

            nuevo_usuario.save()

            return render(req, "inicio.html",{})
        else:
            return render(req,"registro.html",{"mi_formulario" : mi_formulario})
            
    else:
        mi_formulario = UserFormulario()
        return render(req,"registro.html",{"mi_formulario" : mi_formulario})



