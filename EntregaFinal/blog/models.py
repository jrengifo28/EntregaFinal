from django.db import models

# Models


class Pagina(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=256)
    autor = models.CharField(max_length=40)
    fecha = models.DateField()
    imagen = models.FileField()

    def __str__(self):
        return f"Titulo: {self.titulo} Subtitulo: {self.subtitulo} - ({self.autor})"
