"""

A simple function/snippet to read and write basic JSON data.

"""

__version__ = "1.0.1"


import json


def readjson(file_path):
    """Loads and returns JSON data from a local file.

    Args:
        file_path (Path): Local file path to the .json file to read from.

    Returns:
        Data stored in passed JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def writejson(file_path, data) -> None:
    """Writes data contents out to file_path .json file.

    Args:
        file_path (Path): Local file path to the .json file to write to.
        data: JSON compatible data to write to JSON file.
    """
    with open(file_path, "w", encoding="UTF-8") as json_file:
        json.dump(data, json_file, indent=4)
