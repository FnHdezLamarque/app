from django.apps import AppConfig


class PortafolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portafolio'
    #Cambio de nombre al modelo para la vista en el Django admin, se configura en setting.py > del proyecto/carpeta app
    verbose_name = 'Portafolio'