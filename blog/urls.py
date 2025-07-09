from django.urls import path
from . import views

urlpatterns = [
    path('autor/nuevo/', views.crear_autor, name='crear_autor'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('posteo/nuevo/', views.crear_posteo, name='crear_posteo'),
    path('', views.lista_posteos, name='lista_posteos'),  # La lista de posteos, la creamos ahora
    path('buscar/', views.buscar_posteo, name='buscar_posteo'),  # Vista búsqueda (la hacemos ahora)
]
