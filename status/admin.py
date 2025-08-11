from django.contrib import admin
from .models        import Status

# Classes para configurar campos, filtros, busca e etc no admin.
class StatusAdmin(admin.ModelAdmin):
    list_display       = ("id", "descricao",)
    list_display_links = ("id", "descricao",)
    search_fields      = ("descricao",)
    ordering           = ("id",)
    #list_per_page      = 10

# Registrando modelos no admin
admin.site.register(Status, StatusAdmin)