from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('clientapp.urls', namespace='client_app')),
    path('adminapp/', include('adminapp.urls',namespace='admin_app')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
