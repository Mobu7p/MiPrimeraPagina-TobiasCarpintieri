from django import forms
from .models import Autor, Categoria, Posteo

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo', 'contenido', 'autor', 'categoria', 'imagen']

