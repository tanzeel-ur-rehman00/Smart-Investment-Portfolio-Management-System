# bond.py
from investment import Investment

class Bond(Investment):
    """
    Bond investment class representing government or corporate bonds.
    """

    def __init__(self, name, amount, annual_return, years):
        super().__init__(name, amount, annual_return)
        self.years = years

    def calculate_return(self):
        return self.get_amount() * (self.get_annual_return() * self.years)
