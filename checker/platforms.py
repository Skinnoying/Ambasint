import json
import os

def load_platforms():
    json_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Filter hanya entri dictionary yang valid
    valid_data = {}
    for name, details in data.items():
        if isinstance(details, dict) and "url" in details:
            valid_data[name] = details
    return valid_data
