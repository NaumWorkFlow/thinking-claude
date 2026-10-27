"""Currency conversion to USD."""

# Курсы: сколько долларов США стоит 1 единица валюты.
RATES = {
    "USD": 1.0,
    "EUR": 1.08,
    "MDL": 17.8,
}


def to_usd(amount, currency):
    """Convert an amount in the given currency to USD."""
    return amount * RATES[currency]
