class OfficeEquipment:
    name: str = None
    weight: float = float()
    __price: float = None

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except ValueError:
            print(f"price {price} is not a number")
            self.__price = None

    def __str__(self):
        return f'{self.name} {self.price} {self.weight}'