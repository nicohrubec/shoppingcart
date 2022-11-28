import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

class ShoppingCartTest(unittest.TestCase):
    def test_print_receipt_default_format(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("Total: 200", output[1])

    def test_print_receipt_price_first_format(self):
        sc = ShoppingCartConcreteCreator().operation(receipt_format='price-first')
        sc.add_item("apple", 2)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("100 - apple - 2", output[0])
        self.assertEqual("Total: 200", output[1])

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt()
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("banana - 5 - 200", output[1])
        self.assertEqual("pear - 5 - 0", output[2])
        self.assertEqual("Total: 1200", output[3])

unittest.main(exit=False)
