from django.contrib import admin
from django.urls import path, include
# from django.urls import re_path
# from mainapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
]

# это для загрузки картинок и файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

