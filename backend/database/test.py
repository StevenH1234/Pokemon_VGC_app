import os
import requests
import pandas as pd

BASE_URL = "http://pokeapi.co/api/v2"

url = BASE_URL + "/pokedex/2"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["pokemon_entries"])
print(df)

# for i in data["pokemon_entries"]:
#     print(i["pokemon_species"]["name"])
