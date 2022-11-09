from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, blank=True, default=1)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)