import pytest


def test_category(first_category, second_category):
    assert first_category.name == "Category"
    assert first_category.description == "Description of the category"
    assert (
        first_category.get_product_list
        == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт.\n"
    )

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_cat_get_product_list_property(first_category, second_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.get_product_list
        == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт.\n"
    )
    assert (
        second_category.get_product_list
        == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт."
        "\nProduct three, 8467.56 руб. Остаток: 32 шт.\n"
    )


def test_get_product_list(first_category, second_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.get_product_list == "Product, 84.5 руб. Остаток: 10 шт.\n"
        "Product number two, 155.87 руб. Остаток: 34 шт.\n"
    )


def test_category_str(first_category, second_category):
    assert str(first_category) == "Category, количество продуктов: 44 шт."
    assert str(second_category) == "Category number two, количество продуктов: 76 шт."


def test_add_product(first_category, smartphone1, lawn_grass1):
    first_category.add_product(smartphone1)
    assert first_category.products[-1].name == "Samsung Galaxy S23 Ultra"
    first_category.add_product(lawn_grass1)
    assert first_category.products[-1].name == "Газонная трава"


def test_add_error(first_category):
    with pytest.raises(TypeError):
        first_category.add_product(1)


def test_add_smartphone(first_category, smartphone1):
    first_category.add_product = smartphone1


def test_ProductIterator(productiterator):
    iter(productiterator)
    assert productiterator.index == 0
    assert next(productiterator).name == "Product"
    assert next(productiterator).name == "Product number two"

    with pytest.raises(StopIteration):
        next(productiterator)
