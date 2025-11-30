# numpy_utils.py
# This file contains utility functions for NumPy-based calculations.

import numpy as np


def calculate_risk_and_return(investments):
    """
    Calculate average return and portfolio risk using NumPy.
    
    Args:
        investments: List of investment objects
        
    Returns:
        Tuple of (average_return, portfolio_risk)
    """
    if not investments:
        return 0, 0
    
    returns = np.array([inv.get_annual_return() for inv in investments])
    amounts = np.array([inv.get_amount() for inv in investments])
    
    # Calculate weighted average return
    total_amount = np.sum(amounts)
    if total_amount == 0:
        average_return = 0
    else:
        weights = amounts / total_amount
        average_return = np.sum(returns * weights)
    
    # Calculate portfolio risk (standard deviation of returns)
    portfolio_risk = np.std(returns)
    
    return average_return, portfolio_risk
