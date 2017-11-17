from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gallery$', views.dirtree),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
