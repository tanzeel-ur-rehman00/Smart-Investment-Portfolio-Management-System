# investment.py
# This file contains the base Investment class used as an abstract parent.
# All investment types will inherit from this class.

from abc import ABC, abstractmethod

class Investment(ABC):
    """
    Abstract base class representing a general investment.
    Child classes must override calculate_return().
    """

    def __init__(self, name, amount, annual_return):
        # Private attributes to implement Encapsulation
        self.__name = name
        self.__amount = amount
        self.__annual_return = annual_return

    # Getter methods for encapsulated attributes
    def get_name(self):
        return self.__name
    
    def get_amount(self):
        return self.__amount
    
    def get_annual_return(self):
        return self.__annual_return

    # Setter method to update amount
    def set_amount(self, amount):
        self.__amount = amount

    @abstractmethod
    def calculate_return(self):
        """
        Abstract method that child classes must implement.
        """
        pass

    # Operator overloading to demonstrate compile-time polymorphism
    def __add__(self, other):
        return self.__amount + other.__amount
