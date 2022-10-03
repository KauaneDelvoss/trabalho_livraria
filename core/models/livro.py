
from django.db import models


from .autor import Autor
from .categoria import Categoria
from .editora import Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"