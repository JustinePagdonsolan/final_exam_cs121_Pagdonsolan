# user.py
from util.user_manager import UserManager
import os
import time

class User:
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.user_manager = UserManager()

    def register_user(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Registration:\n")
            user_name = input("Kindly enter a username (should be at least 4 characters), leave blank to cancel if ever necessary: ")
            if not user_name:
                return
            if len(user_name) < 4:
                print("The username must be at least 4 characters long...")
                input(" Kindly press enter to continue...")
                continue
            if self.user_manager.is_username_valid(user_name):
                print(" Oops! This username already exists.")
                input(" Kindly press enter to continue...")
                continue
            
            user_password = input("Kindly enter a password (should be at least 8 characters), leave blank to cancel if ever necessary: ")
            if not user_password:
                return
            if len(user_password) < 8:
                print("Oops! The password must be at least 8 characters long...")
                input(" Kindly press enter to continue...")
                continue

            self.user_manager.register_user(user_name, user_password)
            print(" The registration was successful!")
            time.sleep(1)
            return

    def login_user(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Login:\n")
            user_name = input("Kindly enter your username, leave blank to cancel if ever necessary: ")
            if not user_name:
                return
            user_password = input("Kindly enter your password, leave blank to cancel if ever necessary: ")
            if not user_password:
                return
            login_status = self.user_manager.login_user(user_name, user_password)
            if login_status == "Login successful!":
                self.user_name = user_name
                print(login_status)
                time.sleep(1)
                return True
            else:
                print(login_status)
                input("Kindly press enter to continue...")
                continue
