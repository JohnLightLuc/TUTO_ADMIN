from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django_better_admin_arrayfield.models.fields import ArrayField

# from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixi

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField('images')
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    

class Sous_categorie(models.Model):
    nom = models.CharField( max_length=50)
    categore = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='cat')
    image = models.ImageField('images')
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
class Tag(models.Model):
    nom = models.CharField(max_length=50)
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
# class Produit(models.Model):
#     titre= models.CharField(max_length=50)
#     description = models.TextField(max_length=50)
#     image = models.ImageField('images')
#     tag = models.ManyToManyField(Tag)
#     family = JSONField()
#     taille = ArrayField(models.CharField(max_length=200), blank=True)
#     sous_cat = models.ForeignKey(Sous_categorie, on_delete= models.CASCADE, related_name='sous_cat')
#     statut = models.BooleanField(default=False)
#     date_add = models.DateTimeField(auto_now_add=True)
#     date_up = models.DateTimeField(auto_now=True)
    
    

