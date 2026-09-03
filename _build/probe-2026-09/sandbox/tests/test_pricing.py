import pytest

from app.pricing import calculate_final_price


def test_positive_price_and_quantity():
    assert calculate_final_price(10, 3) == 30


def test_zero_quantity_raises():
    with pytest.raises(ValueError):
        calculate_final_price(10, 0)


def test_negative_quantity_raises():
    with pytest.raises(ValueError):
        calculate_final_price(10, -1)
