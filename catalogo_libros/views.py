from django.shortcuts import render, get_object_or_404
from catalogo_libros.models import Libros

# Create your views here.

def listaLibros(request):
    libros = Libros.objects.all()
    return render(request, 'catalogo/lista_libros.html', {'libros': libros})


def detalle_libro(request, id):
    libro = get_object_or_404(Libros, id=id)
    return render(request, 'catalogo/detalle_libro.html', {'libro': libro})