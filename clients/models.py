from django.db import models

# Create your models here.
""" class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, default='Inconnu')
    email = models.EmailField()
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='clients/', null=True, blank=True)
 """


class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, default='Inconnu')
    adresse = models.TextField()
    code_postal = models.CharField(max_length=20)
    ville = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.nom} {self.prenom}"