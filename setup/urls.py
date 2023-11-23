
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from loja_virtual import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('valor.html', views.valor, name='preços'),
    path('imagens.html', views.imagens, name='imagens'),
    path('descrição.html', views.descrição, name='descrição'),
]



