import os, json


class Data:

    def __init__(self, filename):
        self.filename = filename
        self.filepath = os.path.join('data', f'{filename}.json')

        if not os.path.exists(self.filepath):
            raise FileNotFoundError('Data file does not exist.')

    @property
    def data(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    @data.setter
    def data(self, new_data):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=3)

    def get_keys(self):
        try:
            return self.data.keys()
        except:
            return None

    def get_values(self):
        try:
            return self.data.values()
        except:
            return None

    def get_value(self, key):
        try:
            return self.data[str(key)]
        except:
            return None

    def add_value(self, key, value):
        data = self.data
        data[str(key)] = value
        self.data = data

    def remove_value(self, key):
        data = self.data
        del data[str(key)]
        self.data = data

    def reset(self):
        self.data = {}
