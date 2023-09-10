from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
    class Meta():

        verbose_name = 'Course'
        verbose_name_plural = 'The Courses'
        ordering = ('nombre', '-camada')
        unique_together = ('nombre', 'camada')

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50, null=True, blank=True)
    cursos = models.ManyToManyField(Curso)
    
    class Meta():

        verbose_name = 'Profesor'
        verbose_name_plural = 'The Profesors'
        ordering = ('nombre', 'profesion')
        unique_together = ('nombre', 'apellido')    

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=265, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

