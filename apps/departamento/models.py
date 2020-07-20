from django.db import models


class departamento(models.Model):
    nome=models.CharField(max_length=20, help_text='Nome do departamento')

    def __str__(self):
        return self.nome