from django.contrib import admin
from .models import Produit, Categorie
# Register your models here.


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'categorie')
    search_fields = ('nom',)
    list_filter = ('categorie',)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie, CategorieAdmin)