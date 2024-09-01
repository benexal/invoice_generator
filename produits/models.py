from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)  # Ajout du champ Marque
    reference = models.CharField(max_length=255, unique=True)  # Ajout du champ Référence
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)  # Ajout du champ Description
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=4, decimal_places=2)  # Ajout du champ TVA
    

    def __str__(self):
        return self.nom