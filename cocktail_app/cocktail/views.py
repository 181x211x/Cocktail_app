from django.shortcuts import render
from .models import Cocktail,Record_Cocktail,Photo
import csv
from io import TextIOWrapper, StringIO
from .forms import PhotoForm
from django.shortcuts import resolve_url, redirect


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
        data = Cocktail.objects.all()
        params = {
        'cocktail': data,
        }
        return render(request, 'top.html',params)


def search(request):
        return render(request, 'search.html')


def request(request):
        return render(request, 'request.html')


def registration(request):
        return render(request, 'registration.html')

def record(request):

    if request.method == 'GET':
        return render(request, 'record.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.all(),
        })

    elif request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        photo = Photo()
        photo.image = form.cleaned_data['image']
        photo.save()

        return redirect('/cocktail_app/record/')
