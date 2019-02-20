from django.contrib import admin

from .models import Cocktail,Record_Cocktail,Photo


class CocktailAdmin(admin.ModelAdmin):
    fields = ['name', 'base','lengh','tech','alc','taste','material1','material2','contents']

admin.site.register(Cocktail, CocktailAdmin)


class Record_CocktailAdmin(admin.ModelAdmin):
    fields = ['name', 'base','lengh','tech','alc','taste','material1','material2','contents','image']

admin.site.register(Record_Cocktail, CocktailAdmin)

class PhotoAdmin(admin.ModelAdmin):
    fields = ['image']

admin.site.register(Photo, CocktailAdmin)
