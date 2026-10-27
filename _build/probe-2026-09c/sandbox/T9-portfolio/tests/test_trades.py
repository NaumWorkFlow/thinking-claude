import unittest
from pathlib import Path

from app.trades import load_trades

DATA = Path(__file__).resolve().parent.parent / "data" / "trades.csv"


class TestTrades(unittest.TestCase):
    def test_loads_all_rows(self):
        self.assertEqual(len(load_trades(DATA)), 9)


if __name__ == "__main__":
    unittest.main()
