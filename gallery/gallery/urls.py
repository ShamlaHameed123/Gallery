from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gallery/$', views.dirtree),
    url(r'^rate/$', views.rate_photo, name='rate'),
    url(r'^delete/$', views.delete_fe, name='delete_fe'),
    url(r'^delete_photo/$', views.delete_photo, name='delete_photo'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
