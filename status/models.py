from django.db import models

# Create your models here.
class Status(models.Model):
    descricao = models.CharField("Descrição", max_length=150)

    class Meta:
        verbose_name        = "status"
        verbose_name_plural = "status"

    def __str__(self):
        return self.descricao