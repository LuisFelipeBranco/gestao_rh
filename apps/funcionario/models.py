from django.db import models

class funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome completo do funcionario', blank=False)
    cpf = models.CharField(default='000.000.000-00', max_length=14, help_text='CPF do funcionario')

    def __str__(self):
        return self.nome