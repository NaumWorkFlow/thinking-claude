import unittest

from app.api import checkout


class TestCheckout(unittest.TestCase):
    def test_regular_item(self):
        self.assertEqual(checkout("SKU-1", 10, 3), 30)

    def test_regular_item_with_discount(self):
        self.assertEqual(checkout("SKU-1", 10, 3, 5), 25)

    def test_promo_gift_is_free(self):
        self.assertEqual(checkout("PROMO-GIFT", 10, 1), 0)

    def test_sample_box_is_free(self):
        self.assertEqual(checkout("SAMPLE-BOX", 25, 2), 0)


if __name__ == "__main__":
    unittest.main()
