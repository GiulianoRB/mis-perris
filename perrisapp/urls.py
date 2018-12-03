from . import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

app_name = 'perrisapp'
router = routers.DefaultRouter()
router.register(r'api_mascota_listar', views.PerroListarViewSet)


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^formulario/', views.formulario, name="formulario"),
    url(r'^', include(router.urls)),
    url(r'^$', include('rest_framework.urls', namespace='api_mascota_listar'))
]

urlpatterns += staticfiles_urlpatterns()
