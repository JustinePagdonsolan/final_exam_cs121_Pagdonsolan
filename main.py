
from util.user import User
from util.dice_game import DiceGame
import time
import os

def main():

    while True:
        os.system('cls')

        print("Hello and welcome to the *Dice Roll Game*!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Kindly the number of your choice: ")

        
        if choice == "1":
            user = User("", "")
            user.register_user()
        elif choice == "2":
            user = User("", "")
            if user.login_user():
                game = DiceGame(user.user_name)
                game.menu()
        elif choice == "3":
            print("This is now exiting...")
            time.sleep(0.5)
            print("Goodbye! <3")
            exit()
        else:
            print(" Oops! Invalid choice. Kindly try again.")
            time.sleep(1)




if __name__ == "__main__":
    while True:
       main()
