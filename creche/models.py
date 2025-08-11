from django.db       import models
from cadastro.models import Endereco

class TipoUnidade(models.Model):
    sigla = models.CharField("Sigla", max_length=20)

    class Meta:
        verbose_name        = "tipo de unidade"
        verbose_name_plural = "tipo de unidades"

    def __str__(self):
        return f"{self.sigla}"

class Unidade(models.Model):
    nome        = models.CharField("Nome", max_length=150)
    endereco    = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=False)
    tipoUnidade = models.ForeignKey(TipoUnidade, verbose_name="Tp.Unidade", on_delete=models.SET_NULL, null=True, blank=False)
    modalidades = models.ManyToManyField('Modalidade', through='UnidadeModalidade')

    class Meta:
        verbose_name        = "unidade"
        verbose_name_plural = "unidades"

    def __str__(self):
        return self.nome

class Modalidade(models.Model):
    descricao   = models.CharField("Descrição", max_length=150)
    faixaEtaria = models.CharField("Faixa Etária", max_length=150, null=True, blank=True)

    class Meta:
        verbose_name        = "modalidade"
        verbose_name_plural = "modalidades"

    def __str__(self):
        return f"{self.descricao} - {self.faixaEtaria}"

class UnidadeModalidade(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)

    class Meta:
        unique_together     = ('unidade', 'modalidade')