from django.contrib import admin
from .models        import TipoUnidade, Unidade, Modalidade, UnidadeModalidade

# Classes para configurar campos, filtros, busca e etc no admin.
class UnidadeModalidadeInline(admin.TabularInline):
    model = UnidadeModalidade
    extra = 1 # Number of empty forms to display

class ModalidadeAdmin(admin.ModelAdmin):
    list_display       = ("id", "descricao", "faixaEtaria")
    search_fields      = ("descricao", "faixaEtaria")
    list_filter        = ("descricao",)
    #list_per_page      = 10

class TipoUnidadeAdmin(admin.ModelAdmin):
    list_display       = ("id", "sigla",)
    list_display_links = ("id", "sigla",)
    search_fields      = ("sigla",)
    list_filter        = ("sigla",)
    #list_per_page      = 10

class UnidadeAdmin(admin.ModelAdmin):
    inlines = [
        UnidadeModalidadeInline,
    ]

    list_display       = ("id", "nome", "tipoUnidade",)
    list_display_links = ("id", "nome",)
    search_fields      = ("nome",)
    list_filter        = ("nome", "tipoUnidade")
    #list_per_page      = 10

# Registrando modelos no admin
admin.site.register(TipoUnidade, TipoUnidadeAdmin)
admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Modalidade, ModalidadeAdmin)