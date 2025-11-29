# mutualfund.py
from investment import Investment

class MutualFund(Investment):
    """
    Mutual Fund investment class with fund manager charges.
    """

    def __init__(self, name, amount, annual_return, manager):
        super().__init__(name, amount, annual_return)
        self.manager = manager

    def calculate_return(self):
        # Mutual funds add 1% due to professional management
        return self.get_amount() * (self.get_annual_return() + 0.01)
