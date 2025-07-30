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

    print(items)
    print('----')
    print(categories)


def main():
    items_csv()

if __name__=="__main__":
    main()