from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('upload_app.urls')),
    path("accounts/", include("allauth.urls")),
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
