# main.py
# This is the main application file where the system runs.

from user import User
from portfolio import Portfolio
from stock import Stock
from mutualfund import MutualFund
from crypto import Crypto
from realestate import RealEstate
from bond import Bond
from recursion_utils import find_best_investment
from numpy_utils import calculate_risk_and_return


def main():
    print("Welcome to Smart Investment Portfolio Management System")

    users = User.load_users()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            new_user = User(username, password)
            new_user.save_user()
            print("Registration successful.")

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            if username in users and users[username] == password:
                print("Login successful.")

                user = User(username, password)
                portfolio = Portfolio(user)

                # Portfolio actions
                while True:
                    print("\nPortfolio Menu:")
                    print("1. Add Investment")
                    print("2. View Report")
                    print("3. Analyze Portfolio (Recursion + NumPy)")
                    print("4. Logout")

                    c = input("Enter choice: ")

                    if c == "1":
                        print("Choose Investment Type:")
                        print("1. Stock")
                        print("2. Mutual Fund")
                        print("3. Crypto")
                        print("4. Real Estate")
                        print("5. Bond")

                        t = input("Enter type: ")

                        name = input("Investment name: ")
                        amount = float(input("Amount invested: "))
                        rate = float(input("Annual return rate: "))

                        inv = None
                        if t == "1":
                            vol = float(input("Volatility: "))
                            inv = Stock(name, amount, rate, vol)

                        elif t == "2":
                            manager = input("Fund Manager: ")
                            inv = MutualFund(name, amount, rate, manager)

                        elif t == "3":
                            risk = input("Risk level: ")
                            inv = Crypto(name, amount, rate, risk)

                        elif t == "4":
                            loc = input("Property location: ")
                            inv = RealEstate(name, amount, rate, loc)

                        elif t == "5":
                            yrs = int(input("Bond maturity years: "))
                            inv = Bond(name, amount, rate, yrs)
                        
                        else:
                            print("Invalid investment type!")
                            continue

                        if inv is not None:
                            portfolio.add_investment(inv)
                            print("Investment added successfully.")

                    elif c == "2":
                        if not portfolio.investments:
                            print("No investments in portfolio yet!")
                        else:
                            portfolio.generate_report()

                    elif c == "3":
                        if not portfolio.investments:
                            print("No investments in portfolio yet!")
                        else:
                            best = find_best_investment(portfolio.investments)
                            avg, risk = calculate_risk_and_return(portfolio.investments)

                            print("Best Investment:", best.get_name())
                            print("Average Return:", avg)
                            print("Portfolio Risk:", risk)

                    elif c == "4":
                        break

            else:
                print("Invalid credentials.")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
