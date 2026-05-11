"""
file_handler.py

Handles file operations for the project.
"""

import json
import os


class FileHandler:
    """
    Handles loading and saving data.
    """

    FILE_PATH = "data/books.json"

    @staticmethod
    def load_data():
        """
        Loads data from JSON file.
        """
        if not os.path.exists(FileHandler.FILE_PATH):
            return []

        with open(FileHandler.FILE_PATH, "r") as file:
            return json.load(file)

    @staticmethod
    def save_data(data):
        """
        Saves data to JSON file.
        """
        with open(FileHandler.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)