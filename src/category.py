from typing import Any

from src.product import Product


class Category:
    """
    Класс категорий продуктов интернет магазина
    """

    name: str
    description: str
    __products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> list[Any]:
        products_list = []
        for product in self.__products:
            products_list.append(product)
        return products_list

    @property
    def products_list(self) -> str:
        product_list = ""
        for product in self.__products:
            product_list += f"{str(product)}\n"
        return product_list

    def add_product(self, new_product: Product) -> None:
        """
        Добавляем новый продукт в список продуктов
        """
        self.__products.append(new_product)
        Category.product_count += 1
