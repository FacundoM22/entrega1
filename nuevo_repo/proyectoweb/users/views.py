from django.shortcuts import render
from requests import request
from users.models import Familia
from django.http import HttpResponse
import datetime


def inicio(request):
    return render( request, "index.html")




def lista_familiares(request):
    familiares = Familia.objects.all()
    datos = { "datos" : familiares }

    return render(request, "lista_familiares.html", datos)

def alta_familiares(request):
    familiar = Familia(nombre= "Armando", edad=22, nacimiento="1999-05-10")
    familiar.save()
    familiar = Familia(nombre= "Jose", edad=23, nacimiento="1998-02-10")
    familiar.save()
    familiar = Familia(nombre= "Laura", edad=25, nacimiento="1996-06-03")
    familiar.save()
    return HttpResponse("OK")            

                                                                                
##def curso_form(request):

   ## if request.method == "POST":

       ## return render(request, "formulario.html")       