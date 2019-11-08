from django.contrib import admin
from django.utils.safestring import mark_safe

# iptation de modles

from . import models

#-----------------------------Register inline ---------------------

class Sous_CategorieInline(admin.TabularInline):
    model = models.Sous_categorie


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('view_image','nom', 'statut','image', 'date_add', 'date_up')
    list_filter = ('statut', 'date_add','date_up')
    search_fields = ('nom',) 
    date_hierarchy = 'date_add'  
    actions = ('active','desactive')
    list_display_link = ['view_image', 'nom' ]
    list_per_page = 3
    ordering = ['nom']
    #inlines = [Sous_CategorieInline]
    #readonly_fields = ['detail_image']
    
    # ---------------  Fusuionner deu colonnes  ----------------------
    fieldsets = [
        ('Titre et visibilite', {'fields': ['titre', 'statut']})
    ]
        
    # ---------- Many to many------------
    filter_horizontal = ( 'cle etrangere' )
    
    def active(self, request, queryset):
        queryset.update(statut=True) 
        self.message_user(request, "La selection a été activée avexc succes")
        active.description = "Activer les categories selectionnées"
    active.short_description =  ' activer '
    
    def desactive(self, request, queryset):
        queryset.update(statut=False) 
        self.message_user(request, "La selection a été desactivée avexc succes")
        desactive.description = "Desactiver les categories selectionnées "   
    desactive.short_description =  ' Désactiver '
    
    def view_image(sef, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="100px"'.format(img_url=obj.image))
    
    
# @admin.register(models.Sous_categorie)
# class Sous_CategorieAdmin(admin.ModelAdmin):
#     list_display = ('categore','nom', 'statut', 'date_add', 'date_up','image')
#     list_filter = ('statut', 'date_add','date_up','categore')
#     search_fields = ('nom',) 
#     date_hierarchy = 'date_add'  
#     actions = ('active','desactive')
#     list_display_link = ['view_image', 'nom' ]
#     list_per_page = 3
#     ordering = ['nom']
#     extra = 0
    
    
# def active(self, request, queryset):
#     queryset.update(statut=True) 
#     self.message_user(request, "La selection a été activée avexc succes")
#     active.description = "Activer les categories selectionnées"
# active.short_description =  ' activer '
    
# def desactive(self, request, queryset):
#     queryset.update(statut=False) 
#     self.message_user(request, "La selection a été desactivée avexc succes")
#     desactive.description = "Desactiver les categories selectionnées "   
# desactive.short_description =  ' Désactiver '
    
# def view_image(sef, obj):
#     return mark_safe('<img src="{img_url}" width="100px" height="100px"'.format(img_url=obj.image)) 
        

    


    