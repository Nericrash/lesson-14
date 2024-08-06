import pytest

from src.utils import Category, Product


@pytest.fixture
def product() -> Product:
    return Product("Ноутбук", "Высокопроизводительный ноутбук", 1500.0, 10)


@pytest.fixture()
def first_product() -> Product:
    return Product(
        name="Iphone 15", description="Apple Iphone 15", price=1500, quantity=10
    )


@pytest.fixture()
def second_product() -> Product:
    return Product(
        name="Iphone 14", description="Apple Iphone 14", price=1200, quantity=15
    )


@pytest.fixture()
def third_product() -> Product:
    return Product(
        name="Samsung S15", description="Samsung smartphone S15", price=800, quantity=5
    )


@pytest.fixture()
def fourth_product() -> Product:
    return Product(
        name="Samsung S20",
        description="Samsung smartphone S20",
        price=1100,
        quantity=20,
    )


@pytest.fixture()
def first_cat(first_product: Product, second_product: Product) -> Category:
    return Category(
        "Apple", "Смартфоны  компании Apple", [first_product, second_product]
    )


@pytest.fixture()
def second_cat(third_product: Product, fourth_product: Product) -> Category:
    return Category(
        "Samsung", "Смартфоны  компании Samsung", [third_product, fourth_product]
    )
