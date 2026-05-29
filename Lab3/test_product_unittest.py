
import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.towar = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        self.towar.add_stock(5)

        self.assertEqual(self.towar.quantity, 15)

    def test_add_stock_zero(self):
        self.towar.add_stock(0)

        self.assertEqual(self.towar.quantity, 10)

    def test_add_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.towar.add_stock(-3)

    def test_remove_stock_positive(self):
        self.towar.remove_stock(4)

        self.assertEqual(self.towar.quantity, 6)

    def test_remove_stock_all(self):
        self.towar.remove_stock(10)

        self.assertEqual(self.towar.quantity, 0)

    def test_remove_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.towar.remove_stock(-1)

    def test_remove_stock_too_much_raises(self):
        with self.assertRaises(ValueError):
            self.towar.remove_stock(100)

    def test_is_available_when_in_stock(self):
        self.assertTrue(self.towar.is_available())

    def test_is_not_available_when_empty(self):
        pusty_towar = Product("Myszka", 79.99, 0)

        self.assertFalse(pusty_towar.is_available())

    def test_total_value(self):
        self.assertAlmostEqual(self.towar.total_value(), 29999.90)

    def test_price_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            Product("Dziwny produkt", -10.0, 5)

    def test_quantity_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            Product("Klawiatura", 150.0, -2)


if __name__ == "__main__":
    unittest.main()
