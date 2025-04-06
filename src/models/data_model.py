class DataModel:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def remove_data(self, item):
        if item in self.data:
            self.data.remove(item)

    def get_data(self):
        return self.data

    def clear_data(self):
        self.data.clear()