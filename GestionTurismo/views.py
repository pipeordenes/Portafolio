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
    return render(request, 'Cliente.html', {})

def perfil(request):
    return render(request, 'perfil.html', {})