from django.shortcuts import render
from .models import Projet


def accueil(request):
    projets = Projet.objects.all()
    return render(request, 'accueil.html', {'projets': projets})
