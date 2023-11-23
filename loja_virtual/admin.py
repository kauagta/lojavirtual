from django.contrib import admin
from loja_virtual import models 

from models import Categoria,Carros

admin.site.register(Categoria)
admin.site.register(Carros)
