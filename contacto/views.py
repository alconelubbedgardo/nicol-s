from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Su mensaje ha sido enviado"
        else:
            data['form'] = formulario  
       
    return render (request, 'contacto.html', data)