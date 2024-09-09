from src.product import Product


class Smartphone(Product):
    """Товары категории Сматрфоны"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError
