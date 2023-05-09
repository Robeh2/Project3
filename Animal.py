import json
import requests
from Taxonomy import Taxonomy
from Characteristics import Characteristics
from Locations import Locations
from Name import Name

api_key = "Nk2ccUc5OuzZq8iCtfzFJg==riG9B9kOdUqk7HZB"
base_url = "https://api.api-ninjas.com/v1/animals?name="

class Animal:
    """initializes animal class"""
    def __init__(self, name):
        self.name = name
    '''get_name function uses Name class to create name object from Animal'''
    def get_name(self, animal_data):
        name1 = Name(animal_data)
        return name1

    '''get_taxonomy function uses Taxonomy class to create Taxonomy object from Animal'''
    def get_taxonomy(self, animal_data):
        taxonomy = Taxonomy(animal_data)
        return taxonomy

    '''get_characteristics function uses Characteristics class to create Characteristics object from Animal'''
    def get_characteristics(self, animal_data):
        characteristics = Characteristics(animal_data)
        return characteristics

    '''get_locations function uses Locations class to create Locations object from Animal'''
    def get_locations(self, animal_data):
        locations = Locations(animal_data)
        return locations

    '''get_data function pulls the data from the API using api url and key and returns data in json format'''
    def get_data(self):
        final_url = f"{base_url}{self.name}"
        data_pull = requests.get(final_url, headers={'X-Api-Key': api_key})
        data = json.loads(data_pull.text)
        return data