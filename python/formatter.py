
class Formatter:
    """
    Default format for receipts

    To enable more advanced formats the formatting of the whole receipt can be outsourced to this class
    whereas currently only the format of individual receipt rows is defined here
    """
    def __init__(self, delimiter=' - '):
        self.__delimiter = delimiter

    def print_receipt_row(self, item_type: str, amount: int, price: float):
        print(f"{item_type}" + self.get_delimiter() + f"{amount}" + self.get_delimiter() + f"{price}")

    def print_total_row(self, total_price: float):
        print(f"Total: {total_price}")

    def get_delimiter(self):
        return self.__delimiter

class PriceFirstFormatter(Formatter):
    """
    Format that shows the price first on each line
    """
    def print_receipt_row(self, item_type: str, amount: int, price: float):
        print(f"{price}" + self.get_delimiter() + f"{item_type}" + self.get_delimiter() + f"{amount}")
