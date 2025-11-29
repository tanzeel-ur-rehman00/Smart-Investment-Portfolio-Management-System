# user.py
# This file handles registration, login, and storing user credentials.

import os

class User:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.portfolio = None

    def get_username(self):
        return self.__username

    def validate_password(self, password):
        return self.__password == password

    def save_user(self):
        # Saves user credentials to a file for persistence
        with open("data/users.txt", "a") as f:
            f.write(f"{self.__username},{self.__password}\n")

    @staticmethod
    def load_users():
        users = {}
        if os.path.exists("data/users.txt"):
            with open("data/users.txt") as f:
                for line in f:
                    username, password = line.strip().split(",")
                    users[username] = password
        return users
