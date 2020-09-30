from django.contrib import admin
from GestionTurismo.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display=("Nombre","Rut","Email",)
    search_fields=("Nombre","Rut" )


admin.site.register(Cliente, ClienteAdmin)
