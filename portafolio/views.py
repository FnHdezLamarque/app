from django.shortcuts import render
from .models import Project

# Create your views here.
# Se creo una lista para recorrer los titulos de la base de datos
def portafolio(request):
    projects = Project.objects.all()
    return render(request, "portafolio/portafolio.html", {'projects':projects})