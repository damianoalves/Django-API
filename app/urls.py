from django.contrib import admin
from django.urls import path, include

apiurls = [
    path('auth/', include('core.api.urls')),
    path('auth/', include('access.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('core.urls')),
    path('accounts/', include(('access.urls', 'oauth2_provider'), namespace='oauth2_provider')),
    path('api/', include(apiurls)),
]