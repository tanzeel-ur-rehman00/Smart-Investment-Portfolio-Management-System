# stock.py
from investment import Investment

class Stock(Investment):
    """
    Stock investment class representing equity investments.
    """

    def __init__(self, name, amount, annual_return, volatility):
        super().__init__(name, amount, annual_return)
        self.volatility = volatility

    def calculate_return(self):
        # Return calculation specific to stocks
        return self.get_amount() * self.get_annual_return()
