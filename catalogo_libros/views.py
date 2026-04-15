from django.shortcuts import render
from catalogo_libros.models import Libros

# Create your views here.

def listaLibros(request):
    libros = Libros.objects.all()
    return render(request, 'catalogo/lista_libros.html', {'libros': libros})
