from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PosteoForm
from .models import Posteo

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posteos')
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Autor'})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posteos')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nueva Categoría'})

def crear_posteo(request):
    if request.method == 'POST':
        form = PosteoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posteos')
    else:
        form = PosteoForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Posteo'})

from django.db.models import Q

def lista_posteos(request):
    posteos = Posteo.objects.all().order_by('-fecha')
    return render(request, 'blog/lista_posteos.html', {'posteos': posteos})

def buscar_posteo(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Posteo.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        ).order_by('-fecha')
    return render(request, 'blog/buscar.html', {'resultados': resultados, 'query': query})


