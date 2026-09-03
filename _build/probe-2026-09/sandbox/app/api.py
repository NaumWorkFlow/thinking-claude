"""Checkout entrypoint: wires pricing and discounts together."""

from app.pricing import calculate_final_price
from app.discounts import apply_discount


def checkout(base_price, quantity, discount_amount=0):
    total = calculate_final_price(base_price, quantity)
    if discount_amount:
        total = apply_discount(total, discount_amount)
    return total
