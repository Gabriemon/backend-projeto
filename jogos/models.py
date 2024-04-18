from django.db import models

# Create your models here.

class Jogos(models.Model):

    nome = models.CharField(max_length=30)
    data_lancamento = models.CharField(max_length=50)
    preco = models.CharField(max_length=11)

    def __str__(self):
        return self.nome