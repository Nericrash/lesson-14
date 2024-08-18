from src.category import Category
from src.product import Product


def test_category_init(first_cat: Category, second_cat: Category) -> None:
    assert first_cat.name == "Apple"
    assert first_cat.description == "Смартфоны  компании Apple"
    assert len(first_cat.products_list) == 2
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_category_products(first_cat: Category) -> None:
    assert first_cat.products == "Iphone 15, 1500 руб. Остаток: 10 шт.\nIphone 14, 1200 руб. Остаток: 15 шт.\n"


def test_category_products_list(first_cat: Category, first_product: Product, second_product: Product) -> None:
    assert first_cat.products_list == [first_product, second_product]


def test_category_add_product(
    first_cat: Category, first_product: Product, second_product: Product, third_product: Product
) -> None:
    assert first_cat.products_list == [first_product, second_product]
    first_cat.add_product(third_product)
    assert first_cat.products_list == [first_product, second_product, third_product]
