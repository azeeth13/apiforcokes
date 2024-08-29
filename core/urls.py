from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('api.urls')),
    path('api/',include('api.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('dj_rest_auth/',include('dj_rest_auth.urls'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
