from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('product/', include("product.urls")),
    path('', include("user.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)