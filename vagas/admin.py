from django.shortcuts import get_object_or_404
from django.contrib   import admin
from vagas.models     import Lista
from creche.models    import Unidade, Modalidade
from perfil.models    import Perfil
from .forms           import VagasForm

# Register your models here.
class VagasAdmin(admin.ModelAdmin):
    list_display        = ("id", "candidato", "unidade", "modalidade", "dtCadastro", 'status')
    list_display_links  = ("id", "candidato",)
    search_fields       = ("candidato__nome",)
    autocomplete_fields = ("candidato",)
    list_filter         = ("status","unidade",)
    readonly_fields     = ('dtCadastro','dtAtendimento', 'unidadeAtend', )

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            if str(obj.status) in ('Transferido', 'Atendido'):
                return VagasForm
        return super().get_form(request, obj, **kwargs)

    def get_queryset(self, request):
        qs      = super().get_queryset(request)
        perfil  = Perfil.objects.filter(usuario=request.user)
        # perfil  = get_object_or_404(Perfil, usuario=request.user)

        if perfil:
            return qs.filter(unidade=perfil[0].unidade)
        else:
            return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        perfil  = Perfil.objects.filter(usuario=request.user)

        if perfil:
            if db_field.name == "unidade":
                kwargs["queryset"] = Unidade.objects.filter(id=perfil[0].unidade.id)
            if db_field.name == "modalidade":
                kwargs["queryset"] = Modalidade.objects.filter(unidade=perfil[0].unidade)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Lista, VagasAdmin)