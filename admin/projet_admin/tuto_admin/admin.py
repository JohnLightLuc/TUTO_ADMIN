from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget

# Register your models here.


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ( 'view_image', 'nom' , 'image', 'statut', 'date_add', 'date_up')
    list_filter = ('statut', 'date_add', 'date_up')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active', 'desactive')
    list_display_links= ['nom']
    list_per_page = 10
    ordering = ['nom']

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request,"La selection a été activés avec succes")
    
    active.short_description = 'Active'



    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, "La  selection a été bien desactivée")

    desactive.short_description = 'Desactive'

    def view_image(self , obj):
        return mark_safe('<img src = "{url}" width = "100px" heigth = "100px" />'.format(url=obj.image.url))


@admin.register(models.Sous_categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('categore','nom','statut','date_add','date_up','view_image')
    list_filter = ('categore','statut','date_add','date_up')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_display_links = ['nom','view_image']
    list_per_page = 3
    ordering = ['nom']
    #readonly_fields = ['detail_image']

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request,"La selection a été activés avec succes")
    
    active.short_description = 'Active'



    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, "La  selection a été bien desactivée")

    desactive.short_description = 'Desactive'

    def view_image(self , obj):
        return mark_safe('<img src = "{url}" width = "100px" heigth = "100px" />'.format(url=obj.image.url))


# @admin.register(models.Produit)
# class ProduitAdmin(admin.ModelAdmin):
#     list_display = ('sous_cat','titre','statut','date_add','date_up','view_image')
#     list_filter = ('sous_cat','statut','date_add','date_up')
#     search_fields = ('titre',)
#     date_hierarchy = 'date_add'
#     actions = ('active','desactive')
#     list_display_links = ['titre','view_image']
#     list_per_page = 3
#     ordering = ['titre']
#     #filter_horizontal = ('tag',)
#     readonly_fields = ['detail_image']
#     fieldsets = [
#         ('Titre et Visibilité',{
#             'fields':['titre','statut']
#         }),
#         ('Description et image',{
#             'fields':['description','image']
#         }),
#         ('tags et sous Categorie',{
#             'fields':['tag','sous_cat']
#         }),
        
#     ]
#     formfield_overrides = {
#             fields.JSONField: {'widget': JSONEditorWidget},
#     }
    
    
    
    # creation des fonction
    def view_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 250px " heigth = " 350px " />'.format(url=obj.image.url))
   
    def detail_image(self,obj):
        return mark_safe('<img src = "{url}" width = " 100px " heigth = " 100px " />'.format(url=obj.image.url))

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les sousCategorie selectionnés"
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les sousCategorie selectionnés"
    
    
    
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom','statut','date_add','date_up')
    list_filter = ('statut','date_add','date_up')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')
    list_per_page = 3
    ordering = ['nom']
    
    # creation des fonction
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
    
    active.short_description = "activer Les sousCategorie selectionnés"
    
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
        
    desactive.short_description = "desactivés Les sousCategorie selectionnés"

