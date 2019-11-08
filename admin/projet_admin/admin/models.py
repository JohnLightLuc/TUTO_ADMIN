from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField('images')
    statut = models.BooleanField(defauld=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    

class Sous_categorie(models.Model):
    nom = models.CharField(max_length=50)
    categore = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='cat')
    image = models.ImageField('images')
    statut = models.BooleanField(defauld=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
class Tag(models.Model):
    nom = models.CharField(, max_length=50)
    statut = models.BooleanField(defauld=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
class Produit(models.Model):
    titre= models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    image = models.ImageField('images')
    taille = models.PositiveIntegerField()
    tag = models.ManyToManyField(Tag)
    sous_cat = models.ForeignKey(Sous_categorie, on_delete= models.CASCADE, related_name='sous_cat')
    statut = models.BooleanField(defauld=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
    

