import os
import requests
import pandas as pd

BASE_URL = "http://pokeapi.co/api/v2"

url = BASE_URL + "/pokemon/1"

response = requests.get(url)
data = response.json()

# df = pd.DataFrame(data["pokemon_entries"])
print(data.keys())
print(data['name'])
print(data['types'][0]) #probably make a lambda function for this
print([item['ability']['name'] for item in data['abilities']])
print([item['move']['name'] for item in data['moves']])


# while(data['next']):
#     for i in data['results']:
#         print(i['name'])

#     next_group = data['next']
#     response = requests.get(next_group)

#     data = response.json()

