import json

def load_platforms():
    with open("checker/data.json", "r", encoding="utf-8") as f:
        return json.load(f)
