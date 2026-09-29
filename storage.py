import json
import os


def load_data(filename):
    file_path = os.path.join("data", filename)

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        return json.load(file)


def save_data(filename, data):
    file_path = os.path.join("data", filename)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)