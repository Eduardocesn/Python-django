from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/empresas', permanent=False), name='home'),
    path('admin/', admin.site.urls),
    path('home/', include('empresa.urls')),
    path('vagas/', include('vagas.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)