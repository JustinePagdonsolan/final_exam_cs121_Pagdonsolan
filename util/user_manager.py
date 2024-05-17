# user_manager.py
import os

class UserManager:
    def __init__(self):
        self.data_directory = "user_data"
        self.user_data_file = os.path.join(self.data_directory, "users.txt")
        self.create_data_directory()
        
    def create_data_directory(self):
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

    def load_user_data(self):
        user_credentials = {}
        if os.path.exists(self.user_data_file):
            with open(self.user_data_file, "r") as file:
                for line in file:
                    user_name, user_password = line.strip().split(",")
                    user_credentials[user_name] = user_password
        return user_credentials

    def save_user_data(self, user_credentials):
        with open(self.user_data_file, "w") as file:
            for user_name, user_password in user_credentials.items():
                file.write(f"{user_name},{user_password}\n")

    def is_username_valid(self, user_name):
        user_credentials = self.load_user_data()
        return user_name in user_credentials

    def is_password_valid(self, user_name, user_password):
        user_credentials = self.load_user_data()
        return user_credentials[user_name] == user_password

    def register_user(self, user_name, user_password):
        user_credentials = self.load_user_data()
        user_credentials[user_name] = user_password
        self.save_user_data(user_credentials)

    def login_user(self, user_name, user_password):
        if not self.is_username_valid(user_name):
            return "Username does not exist."
        if not self.is_password_valid(user_name, user_password):
            return "Incorrect password. Please try again."
        return "Login successful!"
