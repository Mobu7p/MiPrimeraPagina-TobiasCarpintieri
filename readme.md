# MiPrimeraPagina-Carpintieri

Este es un proyecto web hecho con Django que tiene:

Herencia de plantillas para organizar el diseño.

Tres modelos: Autor, Categoría y Posteo.

Formularios para crear datos en cada modelo.

Lista de posteos con búsqueda por título o contenido.

# Cómo instalar y correr el proyecto

1. 
Clonar o descargar este repositorio.

2.
Crear y activar un entorno virtual con Python:
python -m venv venv
source venv/Scripts/activate

3.
Instalar las dependencias:
pip install -r requirements.txt

4.
Aplicar las migraciones para crear la base de datos:
python manage.py makemigrations
python manage.py migrate

5.
Ejecutar el servidor local:
python manage.py runserver

# Uso de la web
Para crear un autor: ir a /autor/nuevo/
Para crear una categoría: ir a /categoria/nuevo/
Para crear un posteo: ir a /posteo/nuevo/
Para ver todos los posteos: ir a /posteo/
Para buscar posteos: usar la barra de búsqueda en la página de posteos

# Estructura del proyecto
mipagina/ — carpeta del proyecto Django.
blog/ — app con modelos, vistas, formularios y plantillas.
templates/blog/ — archivos HTML.
.gitignore — para ignorar archivos innecesarios.
requirements.txt — listado de dependencias Python.

