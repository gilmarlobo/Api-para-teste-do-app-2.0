from django.db import models

class Registro(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_registro = models.DateTimeField(auto_now_add=True)  # data/hora automática

    def __str__(self):
        return self.nome

# Create your models here.
