"""Line-item pricing for the checkout service."""


def calculate_final_price(base_price, quantity):
    """Calculate the total price for an order line."""
    if quantity <= 0:
        raise ValueError("quantity must be a positive number")
    total = base_price * quantity
    return total
