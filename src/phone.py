from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, couter_sim):
        super().__init__(name, price, quantity)
        self.couter_sim = couter_sim

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError


if __name__ == '__main__':

    dev1 = Item("Aple", 50000, 5)
    dev2 = Phone("Nokia", 60000, 3, 6)
    print(dev2 + dev1)
