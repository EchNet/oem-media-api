from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin123/", admin.site.urls),
    path("content/", include("content.urls")),
    path("api/1.0/", include("content.api.urls")),
    path("api/1.0/", include("core.api.urls")),
    path("test123", TemplateView.as_view(template_name="test.html")),
    path("demo123", TemplateView.as_view(template_name="demoadmin.html")),
    path("ccat123", TemplateView.as_view(template_name="ccat.html")),
]

if settings.SERVE_MEDIA:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
