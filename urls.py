from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Default auth views
    path('', include('myapp.urls', namespace='myapp')),  # Include your app URLs under the 'myapp' namespace
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Custom 404 handler
handler404 = 'myapp.views.custom_404'