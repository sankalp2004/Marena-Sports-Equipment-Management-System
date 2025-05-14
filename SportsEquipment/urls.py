# urls.py (project-level)

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('goods.urls')),  # Assuming you have URLs for 'goods'
    path('goods/', include('goods.urls')),  # Assuming you have URLs for 'goods'
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
