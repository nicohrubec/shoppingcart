from abc import ABC, abstractmethod
from typing import Dict
from collections import OrderedDict

from shopping_cart_interface import IShoppingCart
from pricer import Pricer
from formatter import Formatter, PriceFirstFormatter


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer, formatter: Formatter):
        self.pricer = pricer
        self.formatter = formatter
        self._contents: Dict[str,int] = OrderedDict()

    def get_contents(self):
        return self._contents

    def add_item(self, item_type: str, amount: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            self._contents[item_type] = amount
        else:
            self._contents[item_type] = self._contents[item_type] + amount

    def print_receipt(self):
        total_price = 0

        for item_type, amount in self._contents.items():
            price = self.pricer.get_price(item_type)
            total_price += price * amount
            self.formatter.print_receipt_row(item_type, amount, price)

        self.formatter.print_total_row(total_price)

class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self, receipt_format='default') -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        shopping_cart = self.factory_method()

        # set correct formatter
        if receipt_format == 'default':
            pass
        elif receipt_format == 'price-first':
            shopping_cart.formatter = PriceFirstFormatter()
        else:
            raise NotImplementedError

        return shopping_cart

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer(), Formatter())
