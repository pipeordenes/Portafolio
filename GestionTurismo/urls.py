from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'), 
    path('recuperarcontraseña', views.recuperarcontraseña, name='recuperarcontraseña'), 
    path('registro', views.registro, name='registro'), 
    path('cliente', views.cliente, name='cliente'),

    path('resultado', views.resultado , name='resultado'), 
    path('perfil', views.perfil , name='perfil'), 
    path('servicios', views.servicios , name='servicios'),
    path('reserva', views.reserva , name='reserva'), 
    path('contacto', views.contacto , name='contacto'), 
    path('administrador', views.administrador , name='administrador'),
    path('funcionario', views.funcionario , name='funcionario'),

    path('perfil_funcionario', views.perfil_funcionario , name='perfil_funcionario'),
    path('crear_listado', views.crear_listado , name='crear_listado'), 
    path('mantener_cliente', views.mantener_cliente , name='mantener_cliente'), 
    path('mantener_departamento', views.mantener_departamento , name='mantener_departamento'),
    path('pagos_adm', views.pagos_adm , name='pagos_adm'),
    path('mantener_servicios', views.mantener_servicios , name='mantener_servicios'),
    path('generar_estadistica', views.generar_estadistica , name='generar_estadistica'), 
    path('generar_informe', views.generar_informe , name='generar_informe'), 
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
