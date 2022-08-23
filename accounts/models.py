import email
from random import choices
from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator

from django.contrib.auth.models import AbstractUser

# Create your models here.


opciones_sexo = [
    [0, "Hombre"],
    [1, "Mujer"],
    [2, "Otro"],
    [3, "Prefiero no decirlo"]
]


    
    
class User(AbstractUser):
    """Extiende el Usuario de django"""
    nombre_completo = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(verbose_name="N° DNI", max_length=8,
    validators=[int_list_validator(sep=''),MinLengthValidator(8),], 
    default='27234834')
    telefono = models.CharField(verbose_name="N° Telefono", max_length=10,
    validators=[int_list_validator(sep=''),MinLengthValidator(8),], 
    default='00000000')
    email = models.EmailField('Correo Electronico', max_length=50, null=True)
    sexo = models.IntegerField(choices=opciones_sexo, default='3')
    