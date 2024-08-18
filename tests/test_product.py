from typing import Any
from unittest.mock import patch

from src.product import Product


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "Apple Iphone 15"
    assert first_product.price == 1500
    assert first_product.quantity == 10


def test_product_new_product_duplication(first_product: Product, new_prod_dupl: dict) -> None:
    second_prod = Product.new_product(new_prod_dupl)
    assert second_prod.price == 1500
    assert second_prod.quantity == 35


def test_product_new_product(first_product: Product, new_prod: dict) -> None:
    second_prod = Product.new_product(new_prod)
    assert second_prod.price == 800
    assert second_prod.quantity == 10


def test_product_price(first_product: Product, capsys: Any) -> None:
    assert first_product.price == 1500
    first_product.price = 1700
    assert first_product.price == 1700
    first_product.price = 0
    capture = capsys.readouterr()
    assert capture.out == "Цена не должна быть нулевая или отрицательная\n"
    assert first_product.price == 1700
    first_product.price = -100
    capture = capsys.readouterr()
    assert capture.out == "Цена не должна быть нулевая или отрицательная\n"
    assert first_product.price == 1700

    with patch("builtins.input") as mock_input:
        mock_input.return_value = "y"
        first_product.price = 1300
        assert first_product.price == 1300

    with patch("builtins.input") as mock_input:
        mock_input.return_value = "n"
        first_product.price = 1000
        assert first_product.price == 1300
