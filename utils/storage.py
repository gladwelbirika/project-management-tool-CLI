import json
import os

DATA_FILE = "data/database.json"


def load_data():
    """
    Load data from JSON file.
    If file doesn't exist, return empty structure.
    """
    if not os.path.exists(DATA_FILE):
        return {"users": []}

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """
    Save data to JSON file.
    """
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)