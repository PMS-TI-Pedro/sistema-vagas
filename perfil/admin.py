from django.contrib import admin
from perfil.models  import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display       = ("id", "usuario", "unidade", "membroSec",)
    list_display_links = ("id", "usuario",)
    search_fields      = ("usuario", "unidade", "membroSec",)
    list_filter        = ("usuario", "unidade", "membroSec",)
    #list_per_page      = 10

# Registrando modelos no admin
admin.site.register(Perfil, PerfilAdmin)