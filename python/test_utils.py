from io import StringIO
import sys

def add_items_to_shoppingcart_helper(sc, bought_items):
    """
    Helper that adds a list of items to the given shopping cart.
    :param sc: the shopping cart
    :param bought_items: list of (item_name, amount) tuples
    :return: the updated shopping cart
    """
    for item_type, amount in bought_items:
        sc.add_item(item_type, amount)

    return sc

class Capturing(list):
    """ Helper for capturing the output receipts"""
    _stdout = None
    _stringio = None

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
