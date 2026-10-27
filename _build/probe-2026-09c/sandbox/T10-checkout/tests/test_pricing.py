import unittest

from app.pricing import calculate_final_price


class TestPricing(unittest.TestCase):
    def test_positive_price_and_quantity(self):
        self.assertEqual(calculate_final_price(10, 3), 30)

    def test_zero_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_final_price(10, 0)

    def test_negative_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_final_price(10, -1)


if __name__ == "__main__":
    unittest.main()
