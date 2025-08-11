from django.contrib   import admin
from .models          import Contato, Bairro, Endereco, Responsavel, Candidato
from status.models    import Status
from django.db.models import Q

# Classes para configurar campos, filtros, busca e etc no admin.
class ContatoAdmin(admin.TabularInline):
    model = Contato
    extra = 1

class ResponsavelAdmin(admin.ModelAdmin):
    inlines = [
        ContatoAdmin,
    ]

    list_display       = ("id", "nome", "documento", "endereco", )
    list_display_links = ("id", "nome",)
    list_filter        = ("endereco__bairro",)
    search_fields      = ("nome", "documento",)
    #list_per_page      = 10

class CandidatoAdmin(admin.ModelAdmin):
    list_display        = ("id", "nome", "dtNascimento", "endereco",)
    list_display_links  = ("id", "nome",)
    list_filter         = ("endereco__bairro",)
    search_fields       = ("nome",)

class EnderecoAdmin(admin.ModelAdmin):
    list_display       = ("id", "rua", "numero", "bairro",)
    list_display_links = ("id", "rua",)
    search_fields      = ("rua", "bairro",)
    list_filter        = ("bairro",)
    #list_per_page      = 10

class BairroAdmin(admin.ModelAdmin):
    list_display       = ("nome",)
    list_display_links = ("nome",)
    search_fields      = ("nome",)
    ordering           = ("nome",)
    #list_per_page      = 10

# Registrando modelos no admin
admin.site.register(Bairro, BairroAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(Candidato, CandidatoAdmin)