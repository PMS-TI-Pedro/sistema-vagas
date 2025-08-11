from django.urls import path
from .           import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index, name='index'),
    path('modalidade/lista/<int:pk>', views.ListarModalidade, name='listarModalidades'),
    path('lista/status/<int:unidade>/<int:modalidade>/<int:status>', views.listarVagas, name='listarVagas'),
    path('lista/detalhe/<int:pk>', views.abrirDetalhe, name='detalhe'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)