from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="gauth_app/index.html"), name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
