import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def first_product() -> Product:
    return Product("Iphone 15", "Apple Iphone 15", 1500, 10)


@pytest.fixture()
def second_product() -> Product:
    return Product("Iphone 14", "Apple Iphone 14", 1200, 15)


@pytest.fixture()
def third_product() -> Product:
    return Product("Samsung S15", "Samsung smartphone S15", 800, 5)


@pytest.fixture()
def fourth_product() -> Product:
    return Product("Samsung S20", "Samsung smartphone S20", 1100, 20)


@pytest.fixture()
def first_cat(first_product: Product, second_product: Product) -> Category:
    return Category("Apple", "Смартфоны  компании Apple", [first_product, second_product])


@pytest.fixture()
def second_cat(third_product: Product, fourth_product: Product) -> Category:
    return Category("Samsung", "Смартфоны  компании Samsung", [third_product, fourth_product])


@pytest.fixture()
def new_prod_dupl() -> dict:
    return {"name": "Iphone 15", "description": "Apple Iphone 15", "price": 1200, "quantity": 25}


@pytest.fixture()
def new_prod() -> dict:
    return {"name": "Iphone 13", "description": "Apple Iphone 13", "price": 800, "quantity": 10}
