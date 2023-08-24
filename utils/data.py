import os, json


class Data:
    """
    A class for managing data stored in a JSON file.

    This class represents a data handler for reading and writing data from/to a JSON file. It allows easy access
    to the data stored in the file, as well as updating and adding new key-value pairs.

    Attributes:
        filename (str): The base filename used for the data file (without the file extension).
    """

    def __init__(self, filename):
        self.filename = filename
        self.filepath = os.path.join('data', f'{filename}.json')

        if not os.path.exists(self.filepath):
            raise FileNotFoundError('Data file does not exist.')

    @property
    def data(self):
        """
        Get the data stored in the file.
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    @data.setter
    def data(self, new_data):
        """
        Set the data and store it in the file.
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=3)

    def get_keys(self):
        """
        Get all keys from the data.
        """
        try:
            return self.data.keys()
        except:
            return None

    def get_values(self):
        """
        Get all values from the data.
        """
        try:
            return self.data.values()
        except:
            return None

    def get_value(self, key):
        """
        Get the value for the provided key from the data.
        """
        try:
            return self.data[str(key)]
        except:
            return None

    def add_value(self, key, value):
        """
        Add a new key-value pair to the data and store it.
        """
        data = self.data
        data[str(key)] = value
        self.data = data

    def remove_value(self, key):
        """
        Remove an element from the data.
        """
        data = self.data
        del data[str(key)]
        self.data = data

    def reset(self):
        """
        Reset the data to its initial state with the default values.
        """
        self.data = {}
