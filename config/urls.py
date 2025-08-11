from django.contrib import admin
from django.urls    import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('modalidade/', include('core.urls')),
    path('lista/', include('core.urls')),
    path('admin/', admin.site.urls),
]

#Customizações no Admin
admin.site.site_header = "Controle Lista de Espera"
admin.site.site_title  = "Vagas"
admin.site.index_title = "Configurações"