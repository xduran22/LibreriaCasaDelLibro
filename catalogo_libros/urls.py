from django.urls import path
from catalogo_libros import views

urlpatterns = [
    path('', views.listaLibros, name='lista_libros'),
    path('libros/<int:id>', views.detalle_libro, name='detalle_libro'),
]
