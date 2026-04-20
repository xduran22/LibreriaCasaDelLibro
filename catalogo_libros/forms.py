from .models import Libros
from django import forms

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields  = '__all__'
