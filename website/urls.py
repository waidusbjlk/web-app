from django.conf.urls.static import static

from website import settings
from django.contrib import admin
from django.urls import path, include
from debate.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('debate.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
