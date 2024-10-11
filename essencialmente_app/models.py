from django.db import models
from stdimage.models import StdImageField

class Avaliar_IMC(models.Model):
    cpf = models.FloatField('CPf', blank=False, max_length=11 ,primary_key=True, unique=True)
    nome = models.CharField('Nome',blank=False, max_length=100, )
    sexo = models.CharField('Genero', blank=False,max_length=15)
    data_nasc= models.DateField('Data de Nascimento ',blank=False,)
    escola = models.CharField('Escola Matriculada', blank=False, max_length=200,)
    peso = models.DecimalField('Peso', blank=False,decimal_places=2, max_digits=4)
    altura = models.DecimalField('Altura', blank=False, decimal_places=2,max_digits=3)
    imagem = StdImageField('Imagem do produto',blank=False,variations={'thumb':(124,124)})
    #user:erick 
    #pass:99823580vT