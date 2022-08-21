from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    return render (request, 'contacto.html', data)