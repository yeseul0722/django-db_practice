from django.shortcuts import render
from .models import PetSitter, Pet
# Create your views here.
def get_pet_data():
    pets = Pet.objects.all()
    for pet in pets:
        print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')