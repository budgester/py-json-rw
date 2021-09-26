import json

class Stuff:
    def __init__(self, data = None):
        self.data  = data

    def display_data(self):
        return self.data

    def add_data(self, data):        
        self.data.append(data)

    def load_json(self):
        with open('data.json') as json_file:
            self.data = json.load(json_file)

    def save_json(self):
        with open('data_new.json', 'w') as fp:
            json.dump(self.data, fp)