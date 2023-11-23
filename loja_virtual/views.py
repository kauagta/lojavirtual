from django.shortcuts import render

from setup import urls

def imagens(request):
    return render(request, 'imagens.html')

def descrição(request):
    return render(request, 'descrição.html')

def valor(request):
    return render(request, 'valor.html')