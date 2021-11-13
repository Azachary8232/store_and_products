

class Store():
    def __init__(self, data):
        self.name = data['name']
        self.products = []

    @classmethod
    def add_product(self):
        
