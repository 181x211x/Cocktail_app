from django.shortcuts import render
from .models import Cocktail
import csv
from io import TextIOWrapper, StringIO



def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='Shift_JIS')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            cocktail, created = Cocktail.objects.get_or_create(name=line[1])
            cocktail.name = line[0]
            cocktail.base = line[1]
            cocktail.lengh = line[2]
            cocktail.tech = line[3]
            cocktail.alc = line[4]
            cocktail.taste = line[5]
            cocktail.material1 = line[6]
            cocktail.material2 = line[7]
            cocktail.contents = line[8]
            cocktail.save()

        return render(request, 'upload.html')

    else:
        return render(request, 'upload.html')


def top(request):
        return render(request, 'top.html')


def search(request):
        return render(request, 'search.html')


def request(request):
        return render(request, 'request.html')


def registration(request):
        return render(request, 'registration.html')
