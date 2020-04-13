from django.db import models

class Contenido(models.Model):
    clave = models.CharField(max_length=64)
    valor = models.TextField()

    def __str__(self):
        return self.clave
        
    def tiene_as(self):
        return ('a' in self.valor)

class Comentario(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField(blank=False)
    fecha = models.DateTimeField('publicado')
    
    def __str__(self):
        return self.titulo
        
    def tiene_as(self):
        return ('a' in self.titulo)
