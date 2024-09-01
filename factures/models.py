""" from django.db import models

# Create your models here.

from clients.models import Client
from produits.models import Produit

class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit, through='FactureProduit')

    def __str__(self):
        return f"Facture #{self.id} - {self.client.nom}"

class FactureProduit(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    montant_tva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)  


    @property
    def total(self):
        return self.montant_ttc

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} x {self.prix_unitaire} = {self.total}" """







# models.py

from django.db import models
from clients.models import Client
from produits.models import Produit

class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit, through='FactureProduit')

    def __str__(self):
        return f"Facture #{self.id} - {self.client.nom}"

class FactureProduit(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def montant_ht(self):
        return self.quantite * self.prix_unitaire

    @property
    def montant_tva(self):
        return self.montant_ht * (self.produit.tva / 100)

    @property
    def montant_ttc(self):
        return self.montant_ht + self.montant_tva

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} x {self.prix_unitaire} = {self.montant_ttc}"
