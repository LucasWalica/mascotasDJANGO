from django.db import models
from enum import Enum 


class tipoSprite(Enum):
    Orejon = "orejon"
    Magmitar = "magmitar"

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_de_sprite = models.CharField(max_length=20, choices=[(c.value, c.name) for c in tipoSprite])
    entretenimiento = models.IntegerField(default=10)
    saciedad = models.IntegerField(default=10)
    higiene = models.IntegerField(default=10)
    hp = models.IntegerField(default=100)
    
    