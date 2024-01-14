from django.db import models


class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projets')
    lien = models.URLField(blank=True)

    def __str__(self):
        return self.titre
