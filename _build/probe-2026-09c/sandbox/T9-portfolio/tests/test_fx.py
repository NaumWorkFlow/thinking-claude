import unittest

from app.fx import to_usd


class TestFx(unittest.TestCase):
    def test_usd_is_identity(self):
        self.assertEqual(to_usd(100, "USD"), 100)

    def test_eur(self):
        self.assertAlmostEqual(to_usd(100, "EUR"), 108.0)


if __name__ == "__main__":
    unittest.main()
