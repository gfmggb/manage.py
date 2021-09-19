from django.db import models


class SalaDeAula(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return "Sala de aula #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = "Salas de aula"
