
import requests

from PetHouse_cat_class import Cat

url = 'http://158.160.56.133/api/pet/'
pets = requests.get(url)
pets_list = pets.json()


for pet in pets_list["results"]:
    if pet['species']['code'] == 'cat':
        cat = Cat(name=pet.get("name"), gender=pet.get("gender"), age=pet.get("age"))

print(cat.name)
