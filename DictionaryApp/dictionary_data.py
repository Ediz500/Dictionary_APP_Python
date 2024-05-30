import json

def load_dictionary():
    try:
        with open("dictionary.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_dictionary(dictionary):
    with open("dictionary.json", "w") as file:
        json.dump(dictionary, file)
