from django.contrib import admin

# Register your models here.
from .models import Cocktail,Photo


class CocktailAdmin(admin.ModelAdmin):
    fields = ['name', 'base','lengh','tech','alc','taste','material1','material2','contents','image']

admin.site.register(Cocktail, CocktailAdmin)


class PhotoAdmin(admin.ModelAdmin):
    fields = ['image']

admin.site.register(Photo)
