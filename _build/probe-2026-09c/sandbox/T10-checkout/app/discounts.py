"""Flat discount codes applied before checkout."""


def apply_discount(price, discount_amount):
    """Subtract a flat discount amount from a price."""
    if discount_amount <= 0:
        raise ValueError("discount_amount must be a positive number")
    return price - discount_amount
