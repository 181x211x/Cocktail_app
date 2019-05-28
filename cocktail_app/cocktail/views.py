from django.shortcuts import render
from .models import Cocktail,Record_Cocktail,Photo
import csv
from io import TextIOWrapper, StringIO
from .forms import PhotoForm
from .forms import SearchForm
from .forms import RequestForm
from django.shortcuts import resolve_url, redirect
from . import forms, models
import logging


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
    data = Cocktail.objects.all()
    params = {
    'cocktail': Cocktail.objects.all(),
    'cocktail_form': forms.SearchForm(),
    }
    form = forms.SearchForm(request.POST or None)

    if form.is_valid():
        print(request.POST)
        name = request.POST.getlist('name')
        base = form.cleaned_data['base']
        glass = form.cleaned_data['glass']
        tech = form.cleaned_data['tech']
        taste = form.cleaned_data['taste']
        alc = form.cleaned_data['alc']
        material1 = request.POST.getlist('material1')
        material2 = request.POST.getlist('material2')

        if name == None:
            name = ['']
        if form.cleaned_data['base'] == "全て":
            base = ['']
        if form.cleaned_data['glass'] == "全て":
            glass = ['']
        if form.cleaned_data['tech'] == "全て":
            tech = ['']
        if form.cleaned_data['taste'] == "全て":
            taste = ['']
        if form.cleaned_data['material1'] == None:
            material1 = ['']
        if form.cleaned_data['material2'] == None:
            material2 = ['']
        if form.cleaned_data['alc'] == None:
            alc = 100

        print(name)
        print(base)
        print(glass)
        print(tech)
        print(alc)
        print(material1)
        print(material2)

        if name or base or glass or tech or alc or material1 or material2:
            params = {
            'cocktail': Cocktail.objects.filter(name__contains=name[0],material1__contains=material1[0],material2__contains=material2[0],alc__lte=alc,base__contains=base[0],taste__contains=taste[0],lengh__contains=glass[0],tech__contains=tech[0]),
            'cocktail_form': forms.SearchForm(),
            }


        return render(request, 'search.html',params)

    return render(request, 'search.html',params)


def request(request):

    data = Cocktail.objects.all()
    params = {
    'cocktail_form': forms.RequestForm(),
    }
    form = forms.RequestForm(request.POST or None)

    if form.is_valid():
        print(request.POST)
        taste = form.cleaned_data['taste']
        alc = form.cleaned_data['alc']

        if form.cleaned_data['taste'] == "全て":
            taste = ['']
        if form.cleaned_data['alc'] == "全て":
            max_alc = 100
            min_alc = 0
        elif form.cleaned_data['alc'] == "低め":
            max_alc = 16
            min_alc = 0
        elif form.cleaned_data['alc'] == "そこそこ":
            max_alc = 30
            min_alc = 17
        elif form.cleaned_data['alc'] == "高め":
            max_alc = 50
            min_alc = 31


        print(taste)
        print(alc)

        if taste or alc:
            params = {
            'cocktail': Cocktail.objects.filter(alc__lte=max_alc,alc__gte=min_alc,taste__contains=taste[0]).order_by('?')[:3],
            'cocktail_form': forms.RequestForm(),
            }


        return render(request, 'request.html',params)

    return render(request, 'request.html',params)


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
