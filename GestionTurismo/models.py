from django.db import models

class Clientes(models.Model):

    Nombre=models.CharField(max_length=30)
    Apellidos=models.CharField(max_length=30)
    Edad= models.IntegerField(null=True)
    Nacionalidad=models.CharField(max_length=30)
    Rut=models.CharField(max_length=13)
    Email= models.EmailField(blank=True, null=True)
    Telefono=models.CharField(max_length=12)

    def __str__ (self):
        return self.Nombre

class Departamento(models.Model):

    Nombre_Departamento = models.CharField(max_length=30)
    Numero_propiedad = models.IntegerField(null=True)
    Descripcion= models.CharField(max_length=200, default="")
    Direccion= models.CharField(max_length=200, default="")
    habitaciones = models.IntegerField(null=True)
    Baños = models.IntegerField(null=True)    
    Calefaccion = models.CharField(max_length=2)
    Internet = models.CharField(max_length=2)
    Amoblado = models.CharField(max_length=2)
    Televición = models.CharField(max_length=2)
    Imagen_Recinto = models.ImageField()
    Imagen_Entorno = models.ImageField()
    Valor_Diario = models.IntegerField()
    Disponible = models.CharField(max_length=2)
    Check_in = models.CharField(max_length=200, default="")
    Check_out= models.CharField(max_length=200, default="")

    def __str__ (self):
        return self.Nombre_Departamento 

class Reserva(models.Model):
    Fecha_Reserva_Inicio = models.DateField(null=True, default="") 
    Fecha_Reserva_Termino = models.DateField(null=True, default="") 
    Estado_Reserva = models.CharField(max_length=100, default="")

    def __str__ (self):
        return self.Fecha_Reserva_Inicio

class Transporte(models.Model):

    Trans_Fecha = models.DateField(null=True, default="")
    Trans_Recogida = models.CharField(max_length=200, default="")
    Trans_Destino = models.CharField(max_length=200, default="")
    Trans_Descripcion= models.CharField(max_length=40, default="")
    Tipo_Vehiculo = models.CharField(max_length=200, default="")
    Trans_Costo= models.IntegerField(null=True)

    def __str__ (self):
     return self.Descripcion

class Funcionario(models.Model):

    Nombre=models.CharField(max_length=30)
    Apellidos=models.CharField(max_length=30)
    Nacionalidad=models.CharField(max_length=30)
    Rut=models.CharField(max_length=13)
    DV = models.CharField(max_length=1)
    Email= models.EmailField(blank=True, null=True)

    def __str__ (self):
        return self.Nombre

class ServicioExtra(models.Model):
    Descripcion_Servicio=models.CharField(max_length=200, default="")

    def __str__ (self):
        return self.Descripcion_Servicio

class Turismo(models.Model):

    Tur_Descripcion_Servicio=models.CharField(max_length=200, default="")
    Tur_Fecha=models.DateField(null=True, default="")
    Tur_Valor=models.IntegerField(null=True)

    def __str__ (self):
        return self.Tur_Valor