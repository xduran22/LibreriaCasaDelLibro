from django.urls import path
from catalogo_libros import views

urlpatterns = [
    path('', views.listaLibros, name='libros'),
    path('libros/<int:id>', views.detalle_libro, name='detalle_libro'),
]
