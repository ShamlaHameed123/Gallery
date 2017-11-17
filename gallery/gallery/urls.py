from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gallery$', views.dirtree),
    # url(r'^delete_image/(?P<path>[][0-9]+)/$', views.delete_image),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
