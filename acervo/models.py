from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    data_lancamento = models.IntegerField()
    resumo = models.CharField(max_length=100)
    nome_editora = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    ano_nascimento = models.IntegerField()

    def __str__(self):
        return self.nome