from django.urls import path
from . import views
from .views import ListaPosteosView, DetallePosteoView, EditarPosteoView
from django.urls import path, include


urlpatterns = [
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('posteo/nuevo/', views.crear_posteo, name='crear_posteo'),
    path('', ListaPosteosView.as_view(), name='lista_posteos'), 
    path('buscar/', views.buscar_posteo, name='buscar_posteo'),
    path('posteo/<int:pk>/', DetallePosteoView.as_view(), name='detalle_posteo'),
    path('posteo/<int:pk>/editar/', EditarPosteoView.as_view(), name='editar_posteo'),
    path('posteo/<int:pk>/borrar/', views.borrar_posteo, name='borrar_posteo'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('usuarios/', include('usuarios.urls')),
]
