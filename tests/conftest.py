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


@pytest.fixture
def first_category():
    return Category(
        name="Category",
        description="Description of the category",
        products=[
            Product(
                name="Product",
                description="Description of the product",
                price=84.50,
                quantity=10,
            ),
            Product(
                name="Product number two",
                description="Description of the product number two",
                price=155.87,
                quantity=34,
            ),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Category number two",
        description="Description of the category number two",
        products=[
            Product(
                name="Product",
                description="Description of the product",
                price=84.50,
                quantity=10,
            ),
            Product(
                name="Product number two",
                description="Description of the product number two",
                price=155.87,
                quantity=34,
            ),
            Product(
                name="Product three",
                description="Description of the product three",
                price=8467.56,
                quantity=32,
            ),
        ],
    )


@pytest.fixture()
def new_prod_dupl() -> dict:
    return {"name": "Iphone 15", "description": "Apple Iphone 15", "price": 1200, "quantity": 25}


@pytest.fixture()
def new_prod() -> dict:
    return {"name": "Iphone 13", "description": "Apple Iphone 13", "price": 800, "quantity": 10}


@pytest.fixture
def product_dict():
    return {
        "name": "Product 4",
        "description": "Description of the product 4",
        "price": 145.75,
        "quantity": 23,
    }
