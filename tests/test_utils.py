import json
from typing import List
from unittest.mock import mock_open, patch

from src.utils import Category, Product, get_products_of_json


def test_initialization(product: Product) -> None:
    assert product.name == "Ноутбук"
    assert product.description == "Высокопроизводительный ноутбук"
    assert product.price == 1500.0
    assert product.quantity == 10


def test_quantity_update(product: Product) -> None:
    product.quantity = 5
    assert product.quantity == 5


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Apple"
    assert first_category.description == "Смартфоны  компании Apple"
    assert len(first_category.products) == 2
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_get_products_of_json() -> None:
    mock_data = json.dumps(
        [
            {
                "name": "Категория1",
                "description": "Описание категории 1",
                "products": [
                    {
                        "name": "Продукт1",
                        "price": 100,
                        "description": "Описание1",
                        "quantity": 10,
                    },
                    {
                        "name": "Продукт2",
                        "price": 200,
                        "description": "Описание2",
                        "quantity": 20,
                    },
                ],
            }
        ]
    )

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result: List[Category] = get_products_of_json("test_file.json")

        assert isinstance(result, list)

        assert isinstance(result[0], Category)

        assert result[0].name == "Категория1"
        assert result[0].description == "Описание категории 1"

        assert isinstance(result[0].products[0], Product)
        assert isinstance(result[0].products[1], Product)

        assert result[0].products[0].name == "Продукт1"
        assert result[0].products[0].price == 100
        assert result[0].products[0].description == "Описание1"
        assert result[0].products[0].quantity == 10
        assert result[0].products[1].name == "Продукт2"
        assert result[0].products[1].price == 200
        assert result[0].products[1].description == "Описание2"
        assert result[0].products[1].quantity == 20
