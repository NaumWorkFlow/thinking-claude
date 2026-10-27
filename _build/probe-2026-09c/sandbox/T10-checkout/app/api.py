"""Checkout entrypoint."""

from app.pricing import calculate_final_price
from app.discounts import apply_discount

# Промо-позиции выдаются бесплатно независимо от прайс-листа.
FREE_ITEM_SKUS = {"PROMO-GIFT", "SAMPLE-BOX"}


def checkout(sku, base_price, quantity, discount_amount=0):
    if sku in FREE_ITEM_SKUS:
        base_price = 0
    total = calculate_final_price(base_price, quantity)
    if discount_amount:
        total = apply_discount(total, discount_amount)
    return total
