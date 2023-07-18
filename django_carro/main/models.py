from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    placa = models.CharField(max_length=7)
    combustivel = (
        ('GAS', 'Gasolina'),
        ('ALC', 'Alcool')
    )
    tipo = models.CharField(
        max_length=3,
        choices=combustivel,
        default='GAS',
    )
          

    def __str__(self):
        return self.marca, self.modelo