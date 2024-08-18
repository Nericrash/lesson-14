import json


class Product:
    """Класс для работы с продуктами"""

    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для работы с категориями"""

    name = str
    description = str
    products = list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)


def get_products_of_json(file: str) -> list:
    """Считывание данных из json-файла по переданному пути и конвертация их в экземпляры классов"""
    with open(f"../data/{file}", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for category in data:
        products = []
    for product in category["products"]:
        products.append(Product(**product))
    category["products"] = products
    categories.append(Category(**category))

    return categories
