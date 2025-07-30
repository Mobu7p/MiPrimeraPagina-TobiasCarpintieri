from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PosteoForm
from .models import Posteo
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

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
        form = PosteoForm(request.POST, request.FILES)  # <-- agregá request.FILES
        if form.is_valid():
            form.save()
            return redirect('lista_posteos')
    else:
        form = PosteoForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Posteo'})

from django.db.models import Q

class ListaPosteosView(ListView):
    model = Posteo
    template_name = 'blog/lista_posteos.html'
    context_object_name = 'posteos'
    ordering = ['-fecha']

def buscar_posteo(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Posteo.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        ).order_by('-fecha')
    return render(request, 'blog/buscar.html', {'resultados': resultados, 'query': query})

class DetallePosteoView(LoginRequiredMixin, DetailView):
    model = Posteo
    template_name = 'blog/detalle_posteo.html'
    context_object_name = 'posteo'


class EditarPosteoView(LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = PosteoForm
    template_name = 'blog/formulario.html'
    success_url = reverse_lazy('lista_posteos')

def borrar_posteo(request, pk):
    posteo = get_object_or_404(Posteo, pk=pk)
    if request.method == 'POST':
        posteo.delete()
        return redirect('lista_posteos')
    return render(request, 'blog/confirmar_borrado.html', {'posteo': posteo})

