from django.db import models
from .choices import sexos  # Importa las opciones de sexo desde el archivo choices.py
# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey('Docente',null= True, blank=True,on_delete=models.CASCADE)  # Relación con el modelo Docente
    # Representación en cadena del modelo muestra el nombre del curso 
    def __str__(self):
        texto = " {0} ({1}) "
        return texto.format(self.nombre, self.creditos) # Representación del curso en la interfaz de administración


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)

class Docente(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre del Docente')
    apellido = models.CharField(max_length=100,verbose_name='Apellido del Docente')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    especialidad = models.CharField(max_length=100,verbose_name='Especialidad')
    sexo =  models.CharField(max_length=1, choices= sexos, default = 'F')

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    

    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'  # Nombre de la tabla en la base de datos
        ordering = ['apellido', 'nombre']