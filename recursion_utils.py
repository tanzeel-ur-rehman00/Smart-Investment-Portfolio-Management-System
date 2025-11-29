# recursion_utils.py
# Contains recursive function to find best investment.

def find_best_investment(investments, index=0, best=None):
    if index == len(investments):
        return best

    current = investments[index]

    if best is None or current.get_annual_return() > best.get_annual_return():
        best = current

    return find_best_investment(investments, index + 1, best)
