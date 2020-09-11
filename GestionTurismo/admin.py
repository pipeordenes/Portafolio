from django.contrib import admin
from GestionTurismo.models import Clientes, Departamento, Reserva, Transporte, Funcionario


class ClientesAdmin(admin.ModelAdmin):
    list_display=("Nombre","Rut","Email","Telefono")
    search_fields=("Nombre","Rut" )

class FuncionarioAdmin(admin.ModelAdmin):
    list_display=("Nombre","Rut","Email")
    search_fields=("Nombre","Rut" )

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Departamento)
admin.site.register(Reserva)
admin.site.register(Transporte)
admin.site.register(Funcionario, FuncionarioAdmin)