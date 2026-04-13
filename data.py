import json
import os
FILE = "data.json"
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            data =  json.load(file)
            if "users" not in data:
                data["users"] = {}
            return data
    return {"users": {}}
def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file)
def add_user(name):
    data = load_data()
    if name not in data["users"]:
        data["users"][name] = {"orders": []}
        save_data(data)
def save_order(name, order):
    data = load_data()
    data["users"][name]["orders"].append(order)
    save_data(data)
