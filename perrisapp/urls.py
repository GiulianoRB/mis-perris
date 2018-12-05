from . import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'perrisapp'


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^formulario/', views.formulario, name="formulario"),    
]

urlpatterns += staticfiles_urlpatterns()
