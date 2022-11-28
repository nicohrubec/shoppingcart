
class Formatter:
    """
    Default format for receipts

    To enable more advanced formats the formatting of the whole receipt can be outsourced to this class
    whereas currently only the format of individual receipt rows is defined here
    """
    def __init__(self, delimiter=' - '):
        self.__delimiter = delimiter

    def get_receipt_row(self, item_type: str, amount: int, price: float):
        return f"{item_type}" + self.get_delimiter() + f"{amount}" + self.get_delimiter() + f"{price}"

    def get_total_row(self, total_price: float):
        return f"Total: {total_price}"

    def print_receipt_row(self, item_type: str, amount: int, price: float):
        print(self.get_receipt_row(item_type, amount, price))

    def print_total_row(self, total_price: float):
        print(self.get_total_row(total_price))

    def get_delimiter(self):
        return self.__delimiter

class PriceFirstFormatter(Formatter):
    """
    Format that shows the price first on each line
    """
    def get_receipt_row(self, item_type: str, amount: int, price: float):
        return f"{price}" + self.get_delimiter() + f"{item_type}" + self.get_delimiter() + f"{amount}"
