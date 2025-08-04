from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Autor, Categoria, Posteo

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Posteo)
