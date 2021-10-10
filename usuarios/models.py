from django.db import models
from datetime import datetime

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.EmailField()
    senha = models.CharField(max_length = 64)
    criadoem = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.nome +' - '+ self.email