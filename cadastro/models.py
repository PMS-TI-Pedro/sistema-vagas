from django.db     import models

class Bairro(models.Model):
    nome = models.CharField("Nome", max_length=150)

    class Meta:
        verbose_name        = "bairro"
        verbose_name_plural = "bairros"

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua    = models.CharField("Rua", max_length=150)
    numero = models.CharField("Número", max_length=10, null=True, blank=False)
    bairro = models.ForeignKey(Bairro, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        verbose_name        = "endereço"
        verbose_name_plural = "endereços"

    def __str__(self):
        return f"({self.rua}, {self.numero} - {self.bairro.nome})"

class Responsavel(models.Model):
    nome      = models.CharField("nome", max_length=150)
    documento = models.CharField("Documento", max_length=250, null=True, blank=False)
    endereco  = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        verbose_name        = "responsável"
        verbose_name_plural = "responsáveis"

    def __str__(self):
        return self.nome

class Candidato(models.Model):
    nome          = models.CharField("nome", max_length=150)
    dtNascimento  = models.DateField("Dt.Nascimento")
    responsavel   = models.ForeignKey(Responsavel, on_delete=models.SET_NULL, null=True, blank=False)
    endereco      = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        verbose_name        = "candidato"
        verbose_name_plural = "candidatos"

    def __str__(self):
        return self.nome

class Contato(models.Model):
    ddd         = models.IntegerField("DDD")
    numero      = models.CharField("Número", max_length=250)
    whatsapp    = models.BooleanField("Whatsapp?", null=True, blank=False)
    telegram    = models.BooleanField("Telegram?", null=True, blank=False)
    email       = models.EmailField("E-mail", max_length=250, null=True, blank=False)
    responsavel = models.ForeignKey(Responsavel, related_name="contatos", on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        verbose_name        = "contato"
        verbose_name_plural = "contatos"

    def __str__(self):
        return f"Número: {self.numero}"