import os
import csv 
import requests
import pandas as pd

BASE_URL = "https://pokeapi.co/api/v2"

def saveList(fileName, list):
    with open(fileName, "w") as file:
        for item in list:
            file.write(item + "\n")

def loadList(fileName):
    with open(fileName, "r") as file:
        loadedList = [line.strip() for line in file]
    return loadedList

def create_csv(dictionary, csvName, index_label):
    df = pd.DataFrame(dictionary)
    df.index = df.index+1
    return df.to_csv(csvName, index_label=index_label)

def items_csv():
    item_url = BASE_URL + "/item/"
    items = []
    categories = []

    for i in range(len(loadList("items.txt"))-1):
        url = item_url + str(i+1)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print(f'{i+1} --- {data['name']} : {data['category']['name']}')
            items.append(data['name'])
            categories.append(data['category']['name'])
        else:
            print(f'item {i+1} does not exist')

    item_dict = {"item_name": items,
                 "item_category": categories}
    df = pd.DataFrame(item_dict)
    df.index = df.index + 1
    df.to_csv('items.csv')

    # response = requests.get(item_category_url)
    # data = response.json()
    # print(data['category']['name'])
    
    # store the list of item categories 
    # while item_category_url:
    #     response = requests.get(item_category_url)
    #     data = response.json()
    
    #     for item in data['results']:
    #         categories.append(item['name'])
        
    #     item_category_url = data['next']

    # store the list of all items in the game
    # item_url = BASE_URL + "/item/"
    # while item_url:
    #     response = requests.get(item_url)
    #     data = response.json()
    
    #     for item in data['results']:
    #         items.append(item['name'])
        
    #     item_url = data['next']

    # saveList("categories.txt", categories)
    # saveList("items.txt", items)

def types_csv():
    types_url = BASE_URL + "/type/"
    response = requests.get(types_url)
    data = response.json()
    types = []
    for idx, i in enumerate(data['results']):
        types.append(i['name'])
    
    print(types)
    types_dict = {
        "type_name" : types
    }

    create_csv(types_dict, 'types.csv', index_label='type_id')

def moves_csv():
    moves_url = BASE_URL + "/move/"
    response = requests.get(moves_url)
    data = response.json()
    num_moves = data['count']
    type_id = []
    move_name = []
    base_power = []
    Accuracy = []
    damage_type = []

    df = pd.read_csv("types.csv")
    for i in range(num_moves):
        move_url = moves_url + str(i+1)
        response = requests.get(move_url)
        if response.status_code == 200:
            data = response.json()
            move_name.append(data['name'])
            if data['power'] == "None":
                base_power.append("NULL")
            else:
                base_power.append(data['power'])
            if data['accuracy'] == "None":
                Accuracy.append("NULL")
            else:
                Accuracy.append(data['accuracy'])
            damage_type.append(data['damage_class']['name'])
            type_id.append(df.loc[df["type_name"] == data['type']['name']]['type_id'].values[0])

        else:
            print(f'move {i} not found')

    move_dictionary = {
        "type_id" : type_id,
        "move_name": move_name,
        "base_power": base_power,
        "Accuracy": Accuracy,
        "damage_type": damage_type
    }

    create_csv(move_dictionary, "move.csv", "move_id")

def abilities_csv():
    abilities_url = BASE_URL + '/ability/'
    response = requests.get(abilities_url)
    data = response.json()
    num_abilities = data['count']
    ability_name = []

    for i in range(num_abilities):
        ability_url = abilities_url + str(i+1)
        response = requests.get(ability_url)
        if response.status_code == 200:
            data = response.json()
            ability_name.append(data['name'])
            print(f'{data['name']}')
        else:
            print(f'ability {i+1} does not exist')
    
    ability_dictionary = {
        "ability_name" : ability_name
    }

    create_csv(ability_dictionary, "abilities.csv", "ability_id")

def methods_csv():
    methods_url = BASE_URL + "/move-learn-method/"
    response = requests.get(methods_url)
    data = response.json()
    num_methods = data['count']
    method_name = []

    for i in range(num_methods):
        method_url = methods_url + str(i+1)
        response = requests.get(method_url)
        if response.status_code == 200:
            data = response.json()
            method_name.append(data['name'])
            print(f'{data['name']}')
        else:
            print(f'method {i+1} not found')

    methods_dictionary = {
        "method_name": method_name
    }

    create_csv(methods_dictionary, "methods.csv", "method_id")

def main():
    print("main")
    methods_csv()

if __name__=="__main__":
    main()