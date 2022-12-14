#from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class Libro(models.Model):
    Isbn=models.CharField(max_length=25,primary_key=True)
    titulo=models.TextField(max_length=100,unique=True,null=False)
    editorial=models.CharField(max_length=50,null=False)
    autor=models.CharField(max_length=50,null=False)
    no_page=models.IntegerField(null=False)

    def __str__(self):
        return self.titulo

class Estudiante(models.Model):
    documento=models.IntegerField(primary_key=True)
    nombre=models.TextField(max_length=50,null=False)
    apellidos=models.TextField(max_length=50,null=False)
    email=models.EmailField(unique=True)
    telefono=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellidos

class prestamo(models.Model):
    id=models.AutoField(primary_key=True)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha=models.DateField(auto_now=True)

class Devolucion(models.Model):
    id=models.AutoField(primary_key=True)
    prestamo=models.OneToOneField(prestamo, on_delete=models.CASCADE)
    fecha=models.DateField(auto_now=True)






