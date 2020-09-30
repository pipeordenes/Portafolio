from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['Rut', 'Nombre','Apellidos','Edad','Nacionalidad','Email','Telefono','Nombre_Usuario','Contraseña_Usuario']
