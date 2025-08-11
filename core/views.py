from vagas.models                  import Lista
from creche.models                 import Unidade, Modalidade
from django.shortcuts              import render, get_object_or_404
from django.views.decorators.cache import never_cache

# View responsável pela página inicial/principal.
@never_cache
def Index(request):
    contexto = {}

    unidades = Unidade.objects.all().order_by("tipoUnidade__sigla", "nome")
    contexto['unidades'] = unidades

    if unidades:
        modalidades = Modalidade.objects.filter(unidade__id=unidades[0].id)
        contexto['modalidades'] = modalidades

        if modalidades:
            vagas = Lista.objects.listarVagas(unidades[0], modalidades[0], 1,)
            contexto['vagas'] = vagas

    return render(request, "core/index.html", contexto)

def ListarModalidade(request, pk):
    contexto    = {}
    modalidades = Modalidade.objects.filter(unidade__id=pk).order_by("descricao")
    contexto['modalidades'] = modalidades
    return render(request, "core/seletor.html", contexto)

def listarVagas(request, unidade, modalidade, status,):
    contexto = {}

    vagas = Lista.objects.listarVagas(unidade, modalidade, status, )

    contexto['vagas']   = vagas
    contexto['status']  = status
    return render(request, "core/tabela.html", contexto)

def abrirDetalhe(request, pk):
    contexto   = {}
    detalhe    = get_object_or_404(Lista, pk=pk)

    contexto['detalhe']    = detalhe
    return render(request, "core/detalhe.html", contexto)