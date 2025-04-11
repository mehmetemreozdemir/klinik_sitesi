from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('index.html', TemplateView.as_view(template_name='index.html')),
    path('randevu/', TemplateView.as_view(template_name='randevu.html')),
    path('randevu.html', TemplateView.as_view(template_name='randevu.html')),
    path('blog/', TemplateView.as_view(template_name='blog.html')),
    path('blog.html', TemplateView.as_view(template_name='blog.html')),
    path('iletisim.html', TemplateView.as_view(template_name='iletisim.html')),
    path('doktorlar.html', TemplateView.as_view(template_name='doktorlar.html')),
    path('hizmetler.html', TemplateView.as_view(template_name='hizmetler.html'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    # Ensure static files are properly served during development
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()