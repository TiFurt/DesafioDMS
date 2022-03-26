from django.db import models


# Create your models here.
class Time(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome


class Disputa(models.Model):
    data = models.DateTimeField('data')
    horario = models.TimeField('hora')
    local = models.CharField('local', max_length=100)
    time01 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time01')
    gols01 = models.IntegerField('gols01', default=0)
    time02 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time02')
    gols02 = models.IntegerField('gols02', default=0)

    def __str__(self):
        return f'{self.time01} x {self.time02}'



