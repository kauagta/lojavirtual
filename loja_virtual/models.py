from django.db import models

from loja_virtual import admin

class Categoria(models.Model):
    nome = models.CharField(max_length=10)
    

class Carros(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagens = models.ImageField(upload_to='media')
    valor = models.CharField(max_length=10)
    descrição = models.CharField(max_length=10)