from django.http import HttpResponse

from django.shortcuts import render

from .models import Shoes, Electronics


def Well(request):
    shoes = Shoes.objects.all()
    return render(request, 'home.html', {'allshoes': shoes})
def Smartphone(request):
    electronics = Electronics.objects.all()
    return render (request,'electronics.html',  {'allelectronics': electronics})



