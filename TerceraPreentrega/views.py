from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader

def Tienda(req):
    plantilla = loader.get_template("tienda.html")
    documento = plantilla.render()
    return HttpResponse(documento)


def inicio(req):
    plantilla = loader.get_template("Inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def Formulariocuenta(req):
    return render(req,"inicio_sesion.html")

