from django.shortcuts import render, get_object_or_404, redirect
from catalogo_libros.models import Libros
from catalogo_libros.forms import LibrosForm
from django.contrib import messages

# Create your views here.

def listaLibros(request):
    libros = Libros.objects.all()
    return render(request, 'catalogo/lista_libros.html', {'libros': libros})


def detalle_libro(request, id):
    libro = get_object_or_404(Libros, id=id)
    return render(request, 'catalogo/detalle_libro.html', {'libro': libro})

def crearLibro(request):
    if request.method == 'POST':
        form = LibrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente.')
            form = LibrosForm()
            return redirect('crearLibro')  # Redirige a la misma página para mostrar el formulario vacío después de guardar
        else:
            print(form.errors)  # Esto imprimirá los errores en la consola para depuración
            messages.error(request, 'Corrige errores en rojo')
    else:
        form = LibrosForm()
    return render(request, 'catalogo/crear_libro.html', {'form': form}) 