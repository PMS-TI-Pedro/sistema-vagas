import datetime
from django.db                import models
from django.db.models.signals import pre_save, post_save
from creche.models            import Unidade, Modalidade
from cadastro.models          import Candidato
from status.models            import Status

#Manager's
class ListaManager(models.Manager):
    def listarVagas(self, unidade, modalidade, status,):
        if status in (5,6):
            return Lista.objects.filter(unidade=unidade, modalidade=modalidade, status__in=(4,5),).order_by("-dtCadastro", 'candidato__nome')
        else:
            return Lista.objects.filter(unidade=unidade, modalidade=modalidade, status=status,).order_by("dtCadastro", 'candidato__nome')

# Create your models here.
class Lista(models.Model):
    candidato     = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    unidade       = models.ForeignKey(Unidade, related_name="unidades", on_delete=models.CASCADE)
    modalidade    = models.ForeignKey(Modalidade, on_delete=models.SET_NULL, null=True, blank=False)
    dtCadastro    = models.DateTimeField("Dt.Cadastro", default=datetime.datetime.now)
    status        = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    dtAtendimento = models.DateField("Dt.Atendimento", null=True, blank=True)
    unidadeAtend  = models.ForeignKey(Unidade, related_name="unidade_atend", on_delete=models.SET_NULL, null=True, blank=True)
    observacao    = models.TextField("Observações", max_length=400, null=True, blank=True)

    objects = ListaManager()

    class Meta:
        verbose_name = "lista espera"
        verbose_name_plural = "lista espera"

    def __str__(self):        
        return self.candidato.nome

    class Meta:
       unique_together = ("unidade", "modalidade", "candidato")

# Pre-save
def vagas_pre_save(sender, instance, *args, **kwargs):
    if str(instance.status) in ('Transferido', 'Atendido'):
        instance.dtAtendimento = datetime.datetime.today()
        instance.unidadeAtend  = instance.unidade

pre_save.connect(vagas_pre_save, sender=Lista)

# Post-save
def vagas_post_save(sender, instance, created, *args, **kwargs):
    if str(instance.status) in ('Transferido', 'Atendido'):
        Lista.objects.filter(candidato=instance.candidato, dtAtendimento__isnull=True).update(status=instance.status, unidadeAtend=instance.unidade, dtAtendimento=instance.dtAtendimento, observacao=instance.observacao)

post_save.connect(vagas_post_save, sender=Lista)