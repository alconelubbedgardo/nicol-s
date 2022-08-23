
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
def index(request):
    if request.method == 'POST':
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        asunto=request.POST.get('asunto')
        mensaje=request.POST.get('mensaje')
        
        data = {
            'nombre': nombre,
            'email': email,
            'asunto': asunto,
            'mensaje': mensaje,
        }
        message = '''
        Nuevo mensaje {}
        
        De: {}
        '''.format(data['mensaje'], data['email'])
        send_mail(data['asunto'], mensaje,'noreplay@gmail.com', ['zyckner1994@gmail.com'])
    
    
    return render(request, 'contact/index.html')
    