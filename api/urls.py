from . import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api_perro_listar', views.PerroListarViewSet)
router.register(r'api_adoptador_listar', views.AdoptadorListarViewSet, basename='api')

app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()
