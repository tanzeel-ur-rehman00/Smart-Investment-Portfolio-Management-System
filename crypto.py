# crypto.py
from investment import Investment

class Crypto(Investment):
    """
    Cryptocurrency class representing high-risk digital assets.
    """

    def __init__(self, name, amount, annual_return, risk_level):
        super().__init__(name, amount, annual_return)
        self.risk_level = risk_level

    def calculate_return(self):
        # Crypto returns reduced due to volatility
        return self.get_amount() * (self.get_annual_return() - 0.05)
