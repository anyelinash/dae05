from django.db import models
# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    
    def __str__(self): 
        return self.nombre

class Producto(models.Model): 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200) 
    precio = models.DecimalField(max_digits=6, decimal_places=2) 
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self): 
        return self.nombre

class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    fecha_nac = models.DateField()
    fecha_pub = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"