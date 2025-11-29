# realestate.py
from investment import Investment

class RealEstate(Investment):
    """
    Real Estate investment with an additional 3% appreciation.
    """

    def __init__(self, name, amount, annual_return, location):
        super().__init__(name, amount, annual_return)
        self.location = location

    def calculate_return(self):
        return self.get_amount() * (self.get_annual_return() + 0.03)
