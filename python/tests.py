import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing, add_items_to_shoppingcart_helper
from formatter import Formatter, PriceFirstFormatter

class ShoppingCartTest(unittest.TestCase):

    def check_receipt_printed_correctly(self, receipt, bought_items, pricer, formatter):
        total_price = 0

        for row_idx, (item_type, amount) in enumerate(bought_items):
            self.assertEqual(formatter.get_receipt_row(item_type, amount, pricer.get_price(item_type)),
                             receipt[row_idx])
            total_price += pricer.get_price(item_type) * amount

        self.assertEqual(formatter.get_total_row(total_price), receipt[row_idx + 1])
        self.assertEqual(len(receipt), len(bought_items) + 1)

    def test_print_receipt_default_format(self):
        sc = ShoppingCartConcreteCreator().operation()
        formatter = Formatter()

        bought_items = [("apple", 2)]
        sc = add_items_to_shoppingcart_helper(sc, bought_items)

        with Capturing() as receipt:
            sc.print_receipt()

        self.check_receipt_printed_correctly(receipt, bought_items, sc.pricer, formatter)

    def test_print_receipt_price_first_format(self):
        sc = ShoppingCartConcreteCreator().operation(receipt_format='price-first')
        formatter = PriceFirstFormatter()

        bought_items = [("apple", 2)]
        sc = add_items_to_shoppingcart_helper(sc, bought_items)

        with Capturing() as receipt:
            sc.print_receipt()

        self.check_receipt_printed_correctly(receipt, bought_items, sc.pricer, formatter)

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        formatter = Formatter()

        bought_items = [("apple", 2), ("banana", 5), ("pear", 5)]
        sc = add_items_to_shoppingcart_helper(sc, bought_items)

        with Capturing() as receipt:
            sc.print_receipt()

        self.check_receipt_printed_correctly(receipt, bought_items, sc.pricer, formatter)

    def test_mystery_item_is_free(self):
        sc = ShoppingCartConcreteCreator().operation()

        self.assertEqual(sc.pricer.get_price("unknown-item"), 0)

    def test_unknown_format_raises_notimplemented(self):
        try:
            sc = ShoppingCartConcreteCreator().operation(receipt_format="uknown")
        except NotImplementedError as e:
            pass

    def test_add_one_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        item, amount = "apple", 2
        sc.add_item(item, amount)
        self.assertEqual(sc.get_contents()[item], amount)

    def test_add_one_item_twice(self):
        sc = ShoppingCartConcreteCreator().operation()
        item, amounts = "apple", [2, 3]
        sc.add_item(item, amounts[0])
        sc.add_item(item, amounts[1])
        self.assertEqual(sc.get_contents()[item], amounts[0] + amounts[1])


unittest.main(exit=False)
