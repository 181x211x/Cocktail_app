from django.contrib import admin

from .models import Cocktail


class CocktailAdmin(admin.ModelAdmin):
    fields = ['name', 'base','lengh','tech','alc','taste','material1','material2','contents']

admin.site.register(Cocktail, CocktailAdmin)
