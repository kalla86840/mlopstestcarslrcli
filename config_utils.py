import json
import os

def load_config(path="config.json"):
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir, path)
    with open(config_path, "r") as f:
        return json.load(f)
