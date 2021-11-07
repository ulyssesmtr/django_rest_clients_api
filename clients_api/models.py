from django.db import models

class Client(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=13)
    estado = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    


