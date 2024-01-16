"""

A simple function/snippet to read and write JSON data.

Version = 0.2.0

"""


import json


def load_json_data(file_path) -> dict:
    """Loads and returns JSON data from a local file.

    Args:
        file_path (Path): Local file path to the .json file to read from.

    Returns:
        dict: Dictionary of read JSON data from passed file.
    """
    
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def write_json_file(file_path, data: dict) -> None:
    """Writes data dictionary contents out to file_path .json file.

    Args:
        file_path (Path): Local file path to the .json file to write to.
        data (dict): Dictionary of data to write to JSON file.
    """
    
    with open(file_path, "w", encoding="UTF-8") as json_file:
        json.dump(data, json_file)
        