from django.db import models

# Create your models here.

class Cocktail(models.Model):

    name = models.CharField(max_length=128)
    base = models.CharField(max_length=128)
    lengh = models.CharField(max_length=128)
    tech = models.CharField(max_length=128)
    alc = models.IntegerField(null = True)
    taste = models.CharField(max_length=128)
    material1 = models.CharField(max_length=128,null = True)
    material2 = models.CharField(max_length=128,null = True)
    contents = models.CharField(max_length=128,null = True)
    image = models.ImageField(upload_to='images/',null = True)


class Photo(models.Model):

    image = models.ImageField(upload_to='images/')
