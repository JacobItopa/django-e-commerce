
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(setting.STATIC_URL, document_root = setting.STATIC_ROOT)
    urlpatterns += static(setting.MEDIA_URL, document_root = setting.MEDIA_ROOT)

