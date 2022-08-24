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

opciones_provincia = [
    [0,"Buenos Aires"],
    [1,"CABA"],
    [2,"Catamarca"],
    [3,"Chaco"],
    [4,"Chubut"],
    [5,"Córdoba"],
    [6,"Corrientes"],
    [7,"Entre Ríos"],
    [8,"Formosa"],
    [9,"Jujuy"],
    [10,"La Pampa"],
    [11,"La Rioja"],
    [12,"Mendoza"],
    [13,"Misiones"],
    [14,"Neuquén"],
    [15,"Río Negro"],
    [16,"Salta"],
    [17,"San Juan"],
    [18,"San Luis"],
    [19,"Santa Cruz"],
    [20,"Santa Fe"],
    [21,"Santiago del Estero"],
    [22,"Tierra del Fuego"],
    [23,"Tucumán"]
]


    
    
class User(AbstractUser):
    """Extiende el Usuario de django"""
    
    
    dni = models.CharField(verbose_name="N° DNI", max_length=8,
    validators=[int_list_validator(sep=''),MinLengthValidator(8),])
    telefono = models.CharField(verbose_name="N° Telefono", max_length=10,
    validators=[int_list_validator(sep=''),MinLengthValidator(8),])
    email = models.EmailField('Correo Electronico', max_length=50, null=True)
    sexo = models.IntegerField(choices=opciones_sexo, default='3')
    domicilio = models.CharField(max_length=50, null=True)
    provincia = models.IntegerField(choices= opciones_provincia, default='3')
    