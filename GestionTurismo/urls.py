from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'), 
    path('recuperarcontraseña', views.recuperarcontraseña, name='recuperarcontraseña'), 
    path('registro', views.registro, name='registro'), 
    path('cliente', views.cliente, name='cliente'), 
    path('perfil', views.perfil , name='perfil'), 


]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
