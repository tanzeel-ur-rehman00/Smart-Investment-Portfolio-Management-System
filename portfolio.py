# portfolio.py
# This file represents a user's portfolio containing multiple investments.

class Portfolio:

    def __init__(self, owner):
        self.owner = owner
        self.investments = []

    def add_investment(self, inv):
        self.investments.append(inv)

    def total_value(self):
        return sum(inv.get_amount() for inv in self.investments)

    def total_returns(self):
        return sum(inv.calculate_return() for inv in self.investments)

    def generate_report(self):
        print("----- Portfolio Report -----")
        print("Owner:", self.owner.get_username())
        print("Total Investment Value:", self.total_value())
        print("Total Expected Returns:", self.total_returns())
