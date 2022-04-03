from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('houses', views.houses, name="houses"),
    path('search', views.search, name="search"),
    path('<int:house_id>', views.house, name="house"),
    path('contact', views.contact, name="contact")
]