from django.shortcuts import render
from django.http import HttpResponse
from proyectoapp.models import Familia
from django.template import loader

# Create your views here.

def fam (request):

    family = Familia.objects.all()
    family.delete()

    familiar1 = Familia(parentesco = "Padre", nombre = "Beltran", edad =68, nacimiento = "1954-12-15")
    familiar1.save()

    familiar2 = Familia(parentesco = "Madre", nombre = "Florencia", edad =62, nacimiento = "1960-07-11")
    familiar2.save()

    familiar3 = Familia(parentesco = "Hermana", nombre = "Evelyn", edad =38, nacimiento = "1983-09-22")
    familiar3.save()

    documento = f"Mi familia es: Mi {familiar1.parentesco} es {familiar1.nombre} su edad es {familiar1.edad} y nacio el {familiar1.nacimiento}...Mi {familiar2.parentesco} es {familiar2.nombre} su edad es {familiar2.edad} y nacio el {familiar2.nacimiento}...Mi {familiar3.parentesco} es {familiar3.nombre} su edad es{familiar3.edad} y su fecha de naciomento es {familiar3.nacimiento}"

    family = Familia.objects.all()

    obj = {"familias":family}

    return render (request,"plantilla1.html",obj)


    #diccionario = f"Mi familia es: Mi {familiar1.parentesco} es {familiar1.nombre} su edad es {familiar1.edad} y nacio el {familiar1.nacimiento}...Mi {familiar2.parentesco} es {familiar2.nombre} su edad es {familiar2.edad} y nacio el {familiar2.nacimiento}...Mi {familiar3.parentesco} es {familiar3.nombre} su edad es{familiar3.edad} y su fecha de naciomento es {familiar3.nacimiento}"

    #plantilla = loader.get_template("plantilla1.html")

    #documentoDeTexto = plantilla.render(diccionario)

    #return HttpResponse (documento)