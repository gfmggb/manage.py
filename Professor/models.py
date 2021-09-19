from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length = 45)
    cpf = models.CharField(max_length = 15)
       def __str__(self):
        return "Professor #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = "professores"
