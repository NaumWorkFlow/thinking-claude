"""Loading trades exported from the broker."""

import csv
from dataclasses import dataclass
from datetime import date


@dataclass
class Trade:
    trade_id: int
    date: date
    ticker: str
    side: str  # "BUY" or "SELL"
    qty: int
    price: float
    currency: str
    fee: float


def load_trades(path):
    """Read trades from a broker CSV export, in file order."""
    trades = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            trades.append(
                Trade(
                    trade_id=int(row["trade_id"]),
                    date=date.fromisoformat(row["date"]),
                    ticker=row["ticker"],
                    side=row["side"],
                    qty=int(row["qty"]),
                    price=float(row["price"]),
                    currency=row["currency"],
                    fee=float(row["fee"]),
                )
            )
    return trades
