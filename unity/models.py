from django.db import models

# Create your models here.

# class Clientes(models.Model):
#     nombre=models.CharField(max_length=30)
#     direccion=models.CharField(max_length=30)
#     email=models.EmailField()#metodo especial para la creacion de correos electronicso
#     tfono=models.CharField(max_length=7)

class Pelicula(models.Model):
    Titulo=models.CharField(max_length=30) #campo clave
    Categoria=models.CharField(max_length=30)
    Pais=models.CharField(max_length=30)
    Lenguaje=models.CharField(max_length=30)
    Director=models.CharField(max_length=30)
    Sinopsis=models.CharField(max_length=30) #campo clave
    Duracion=models.CharField(max_length=30) #campo clave
    Caratula=models.CharField(max_length=30) #no se como, sera llamarlo con el nombre del archibvo image.png y pasarlo como parametro para que lo llame Django
    

class Sala(models.Model):
    Puestos=models.CharField(max_length=30)
    pantalla=models.CharField(max_length=30)
    Nombre=models.CharField(max_length=30)
    
    

# class pedidos(models.Model):
#     numero=models.IntegerField()
#     fecha=models.DateField()              #un metodo para la creacion de date
#     entregado=models.BooleanField()

#flata la clase boleto
# Create your models here.
