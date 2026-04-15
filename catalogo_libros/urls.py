from django.urls import path
from catalogo_libros import views

urlpatterns = [
    path('', views.listaLibros, name='lista_libros'),
]