from django.shortcuts import render
from .models import *

choices = TYPE_CHOICES

houses_cities = House.objects.all()
cities =[]
for house in houses_cities:
    if house.city not in cities:
        cities.append(house.city)

def index(request):
    houses = House.objects.all()
    context = {'houses': houses, 'choices': choices, 'cities':cities}
    return render (request, 'Real_Estate/index.html', context)

def houses(request):
    houses = House.objects.all()
    context = {'houses': houses}
    return render (request, 'Real_Estate/houses_list.html', context)

def search(request):
    type = request.POST.get('type')
    area = request.POST.get('area')
    city = request.POST.get('city')
    price = request.POST.get('price')

    houses = House.objects.filter(price__lte = price, area__lte = area, type = type, city = city)
    context = {
        'houses': houses, 
        'search': True, 
        'choices': choices,
        'type': type,
        'area': area,
        'city': city,
        'price': price,
        'cities':cities
        }
    return render (request, 'Real_Estate/houses_list.html', context)

def house(request, house_id):
    house = House.objects.get(id = house_id)
    images = Images.objects.filter(house = house)

    context = {'house': house, 'images': images, 'choices': choices, 'FLOOR_CHOICES': FLOOR_CHOICES}
    return render (request, 'Real_Estate/house.html', context)

def contact(request):
    return render (request, 'Real_Estate/contact.html', {})