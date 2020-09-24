from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    return render(request, 'index.html', context={},)

def login(request):
    return render(request, 'login.html', {})

def recuperarcontraseña(request):
    return render(request, 'recuperarcontraseña.html', {})

def registro(request):
    return render(request, 'registro.html', {})

def cliente(request):
    return render(request, 'cliente.html', {})

def perfil(request):
    return render(request, 'perfil.html', {})

def servicios(request):
    return render (request, 'servicios.html')

def reserva(request):
    return render (request, 'reserva.html')

def funcionario(request):
    return render (request, 'funcionario.html')


def perfil_funcionario(request):
    return render (request, 'perfil_funcionario.html')
    
def crear_listado(request):
    return render (request, 'crear_listado.html')
    

def contacto_funcionario(request):
    return render (request, 'contacto_funcionario.html')

