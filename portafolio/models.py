from django.db import models

# Create your models here.
#Modelo de insercion de proyectos
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #upload project define donde guardar la imagen
    image = models.ImageField(upload_to="project")
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        #cambio del nombre del modelo (BD)
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        #Orden del acomodo de los registros "-" indica que sera de orden ascendente y "created" ordena por fecha de creacion
        ordering = ["-created"]
    
    #Esta funcion muestra el campo titulo como nombre del proyecto en Django Admin
    def __str__(self):
        return self.title # pylint: disable=invalid-str-returned