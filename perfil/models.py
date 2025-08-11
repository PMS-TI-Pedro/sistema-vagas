from django.contrib.auth.models import User
from django.db                  import models
from creche.models              import Unidade

class Perfil(models.Model):
    usuario   = models.ForeignKey(User, on_delete=models.CASCADE)
    unidade   = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True, blank=True)
    membroSec = models.BooleanField("Membro da secretaria?", default=False)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfis"

    def __str__(self):
        return f"usuário {self.usuario.username}"