from dataclasses import field
from socket import fromshare
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        field = '__all__'