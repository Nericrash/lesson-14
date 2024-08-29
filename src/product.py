class Product:
    """Продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.quantity * self.price + other.quantity * other.price

    @classmethod
    def new_product(cls, new_product: dict):
        """Взвращает созданный объект класса Product из параметров товара в словаре"""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или орицательная")
        else:
            self.__price = value

            from src.category import Category
            from src.product import Product

            class ProductIterator:
                """Класс для итерации товаров одной категории"""

                def __init__(self, category_obj):
                    self.category = category_obj
                    self.index = 0

                def __iter__(self):
                    return self

                def __next__(self):
                    if self.index < len(self.category.products):
                        prod = self.category.products[self.index]
                        self.index += 1
                        return prod
                    else:
                        raise StopIteration

            if __name__ == "__main__":
                product1 = Product(
                    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
                )
                product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
                product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

                category1 = Category(
                    "Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    [product1, product2, product3],
                )

                iterator = ProductIterator(category1)
                for product in iterator:
                    print(product)
