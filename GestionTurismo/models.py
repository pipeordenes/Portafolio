from django.db import models

class Cliente(models.Model):
    Rut=models.CharField(max_length=14, unique=True)
    Nombre=models.CharField(max_length=30, null=True)
    Apellidos=models.CharField(max_length=30, null=True)
    Edad= models.IntegerField(null=True)
    Nacionalidad=models.CharField(max_length=30, null=True)
    Email= models.EmailField(blank=True, null=True)
    Telefono=models.CharField(max_length=12, null=True)
    Nombre_Usuario=models.CharField(max_length=12, default="")
    Contraseña_Usuario=models.CharField(max_length=12, default="")
    

    def __str__ (self):
        return self.Nombre
