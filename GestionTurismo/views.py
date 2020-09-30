from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.db import connection
from .models import Cliente
from .forms import ClienteForm
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', context={},)

def login(request):
    return render(request, 'login.html', {})

def recuperarcontraseña(request):
    return render(request, 'recuperarcontraseña.html', {})

def registro(request):
    return render(request, 'registro.html', {})

def perfil(request):
    return render(request, 'perfil.html', {})

def servicios(request):
    return render (request, 'servicios.html')

def reserva(request):
    return render (request, 'reserva.html')

def contacto(request):
    return render (request, 'contacto.html')

def administrador(request):
    return render (request, 'administrador.html')

def funcionario(request):
    return render (request, 'funcionario.html')

def perfil_funcionario(request):
    return render (request, 'perfil_funcionario.html')
    
def crear_listado(request):
    return render (request, 'crear_listado.html')

def mantener_cliente(request):
    return render (request, 'mantener_cliente.html')

def mantener_departamento(request):
    return render (request, 'mantener_departamento.html')

def pagos_adm(request):
    return render (request, 'pagos_adm.html')

def mantener_servicios(request):
    return render (request, 'mantener_servicios.html')
    
def generar_estadistica(request):
    return render (request, 'generar_estadistica.html')

def generar_informe(request):
    return render (request, 'generar_informe.html')

def resultado(request):
    return render (request, 'resultado.html')

def cliente(request):
    return render(request, 'cliente.html', {})

def registro(request):
    form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/resultado')
    return render(request, "registro.html", {'form': form})
