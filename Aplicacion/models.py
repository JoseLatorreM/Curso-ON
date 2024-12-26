from django.db import models

class usuarios(models.Model):
    Rut = models.CharField(max_length=12, primary_key=True)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Contraseña = models.CharField(max_length=100)

class cursos(models.Model):
    NCurso = models.CharField(max_length=200)
    Autor = models.CharField(max_length=100)
    Duracion = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    Dificultad = models.CharField(max_length=50, default="Desconocida")
    Categoria = models.CharField(max_length=50, default="Desconocida")
    DesDet = models.TextField(800, default="Desconocida")
    NumUnidades = models.IntegerField()
    ImagenPortada = models.ImageField(upload_to='Portadas/', null=True, blank=True)
    
class Unidad(models.Model):
    curso = models.ForeignKey(cursos, on_delete=models.CASCADE, related_name="unidades")
    nombre = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='unidades_imagenes/', null=True, blank=True)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    curso = models.ForeignKey(cursos, related_name="Comentarios", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Comentario de {self.usuario.Nombre} sobre {self.curso.NCurso}"
    
