from django.db import models

class Clientes(models.Model):

    Nombre=models.CharField(max_length=30)
    Apellidos=models.CharField(max_length=30)
    Edad= models.IntegerField()
    Nacionalidad=models.CharField(max_length=30)
    Rut=models.CharField(max_length=13)
    Email= models.EmailField(blank=True, null=True)
    Telefono=models.CharField(max_length=12)

    def __str__ (self):
        return self.Nombre

class Departamento(models.Model):

    Nombre_Departamento = models.CharField(max_length=30)
    Numero_propiedad = models.IntegerField()
    Descripcion= models.CharField(max_length=200)
    Direccion= models.CharField(max_length=200)
    habitaciones = models.IntegerField()
    Baños = models.IntegerField()    
    Calefaccion = models.CharField(max_length=2)
    Internet = models.CharField(max_length=2)
    Internet = models.CharField(max_length=2)
    Amobla = models.CharField(max_length=2)
    Televición = models.CharField(max_length=2)
    Imagen_Recinto = models.ImageField()
    Imagen_Entorno = models.ImageField()
    Valor_Diario = models.IntegerField()
    Disponible = models.CharField(max_length=2)
    Check_in = models.CharField(max_length=200)
    Check_out= models.CharField(max_length=200)

    def __str__ (self):
        return self.Nombre_Departamento 

class Reserva(models.Model):
    Fecha_Reserva_Inicio = models.DateField() 
    Fecha_Reserva_Termino = models.DateField() 
    Estado = models.CharField(max_length=100)

    def __str__ (self):
        return self.Fecha_Reserva_Inicio

class Transporte(models.Model):

    Fecha = models.DateField()
    Recogida = models.CharField(max_length=200)
    Destino = models.CharField(max_length=200)
    Descripcion= models.CharField(max_length=40)
    Tipo_Vehiculo = models.CharField(max_length=200)
    Costo= models.IntegerField()

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

    Descripcion_Servicio=models.CharField(max_length=200)
    Tipo=models.CharField(max_length=30)
    Valor=models.IntegerField()

    def __str__ (self):
        return self.Tipo

class Turismo(models.Model):

    Descripcion_Servicio=models.CharField(max_length=200)
    Fecha=models.DateField()
    Valor=models.IntegerField()

    def __str__ (self):
        return self.Valor