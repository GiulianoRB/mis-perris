from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('perrisapp.urls')),    
    url(r'^formulario/', include('perrisapp.urls')),
    path('', include('pwa.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('api.urls')),
]
