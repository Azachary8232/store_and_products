


class Products():
    def __init__(self, data):
        self.name = data['name']
        self.price = data['price']
        self.category = data['category']
    

    @classmethod
    def update_price(self, rate_change):
        if rate_change > 0:
            self.price = self.price + (self.price * rate_change)
        else:
            self.price = self.price - (self.price * rate_change)

    @classmethod
    def print_info(self):
        print(self.name, self.category, self.price)