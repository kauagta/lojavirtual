from django.shortcuts import render


def preços(request):
    return render(request, 'preços.html')