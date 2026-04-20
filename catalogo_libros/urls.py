from django.urls import path
from catalogo_libros import views

urlpatterns = [
    path('', views.listaLibros, name='libros'),  # Nota que aquí no hay barra al final en path ''.
    path('libros/<int:id>', views.detalle_libro, name='detalle_libro'),
    path('crear/', views.crearLibro, name='crearLibro'),
]
