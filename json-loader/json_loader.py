"""

A simple function/snippet to load and return JSON 
data so I don't have to type it over and over again.

Version = 0.1.0

"""


import json


def load_json_data(file_path) -> dict:
    """Loads and returns JSON data from a local file.

    Args:
        file_path (Path): Local file path to the .json file to read from.

    Returns:
        dict: Dictionary of read JSON data from passed file.
    """
    
    with open(file_path, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)
