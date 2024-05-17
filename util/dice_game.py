# dice_game.py
import os
import time
import random
from util.score import Score

class DiceGame:

    def __init__(self, username):
        self.username = username
        self.score_folder = "scores"
        self.score_file = os.path.join(self.score_folder, "rankings.txt")
        self.create_score_folder()
        self.score = Score(self.username, "")



    def create_score_folder(self):
        if not os.path.exists(self.score_folder):
            os.makedirs(self.score_folder)



    def load_scores(self):
        scores = []
        try:
            if os.path.exists(self.score_file):
                with open(self.score_file, "r") as file:
                    for line in file:
                        username, score, stage_score, date = line.strip().split(",")
                        scores.append((username, int(score), int(stage_score), date))
            return scores
        except FileNotFoundError:
            return None



    def save_scores(self, scores):
        with open(self.score_file, "w") as file:
            for username, score, stage_score, date in scores:
                file.write(f"{username},{score},{stage_score},{date}\n")



    def continue_game(self):
        while True:
            cont = input("\nDo you want to continue to the next stage? (1 for Yes, 0 for No): ")
            if cont == "1":
                return True
            if cont == "0":
                return False
            else:
                print(" Oops! This is an invalid input. Kindly enter 1 for Yes or 0 for No.")
                input("Kindly press enter to continue...")
                continue



    def play_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Starting game as {self.username}...")
        cpu_points = 0
        user_points = 0
        stage_wins = 0


        while True:
            for _ in range(3):
                cpu_roll = random.randint(1, 6)
                user_roll = random.randint(1, 6)

                print(f"{self.username} rolled: {user_roll}")
                print(f"CPU rolled: {cpu_roll}")
                if cpu_roll < user_roll:
                    user_points += 1
                    print(f"You win this round, {self.username}!\n")
                elif cpu_roll > user_roll:
                    cpu_points += 1
                    print("CPU wins this round!\n")
                else:
                    print("It's a tie!\n")
                time.sleep(1)


            while cpu_points == user_points:
                cpu_roll = random.randint(1, 6)
                user_roll = random.randint(1, 6)

                print(f"{self.username} rolled: {user_roll}")
                print(f"CPU rolled: {cpu_roll}")
                if cpu_roll < user_roll:
                    user_points += 1
                    print(f"Hey! You win this round, {self.username}!\n")
                elif cpu_roll > user_roll:
                    cpu_points += 1
                    print("Woah, CPU wins this round!\n")
                else:
                    print("Not bad! It's a tie!\n")
                time.sleep(1)


            if cpu_points < user_points:
                user_points += 3
                stage_wins += 1
                self.score.update_score(user_points, stage_wins)
                user_points, cpu_points = self.score.reset_current_score()
                print(f"\nYou won this stage, {self.username}!\n")



                if self.continue_game():
                    continue
                else:
                    top_scores = self.load_scores() or []
                    top_scores.append(self.score.to_record())
                    top_scores.sort(key=lambda x: x[1], reverse=True)
                    top_scores = top_scores[:10]
                    self.save_scores(top_scores)
                    self.score.reset_all_scores()
                    if stage_wins < 1:
                        print(f"Looks like it's Game Over. You won {stage_wins} stage.")
                    else:
                        print(f"Looks like it's Game Over. You won {stage_wins} stages.")
                    break



            if cpu_points > user_points:
                user_points, cpu_points = self.score.reset_current_score()
                if stage_wins == 0:
                    print(f"\nYou lost this stage.\n")
                    print("Looks like it's Game Over... You didn't win any stages...")
                else:
                    self.score.update_score(user_points, 0)
                    top_scores = self.load_scores() or []
                    top_scores.append(self.score.to_record())
                    top_scores.sort(key=lambda x: x[1], reverse=True)
                    top_scores = top_scores[:10]
                    self.save_scores(top_scores)
                    self.score.reset_all_scores()
                    print("Oops! It looks like you lost this stage.")
                    if stage_wins < 1:
                        print(f"Looks like it's game over. You won {stage_wins} stage.")
                    else:
                        print(f"Looks like it's game over. You won {stage_wins} stages.")
                input(" Kindly press enter to continue...")
                break

 

    def show_top_scores(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Here are the top Scores:")
        scores = self.load_scores()
        if not scores:
            print("There are no games played yet. Play a game to see top scores!")
        else:
            for index, (username, score, stage_score, date) in enumerate(scores, start=1):
                print(f"{index}. {username}: Points - {score}, Wins - {stage_score} (Achieved on: {date})")
        input(" Kindly press enter to continue...")



    def logout(self):
        print(f"Goodbye, dear {self.username}")
        print("You logged out successfully.")
        time.sleep(1)
        return True



    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Welcome, {self.username}")
            print("Menu:")
            print("1. Start Game")
            print("2. Show Top Scores")
            print("3. Log Out")
            choice = input("Kindly enter the number of your choice: ")

            if choice == "1":
                self.play_game()
            elif choice == "2":
                self.show_top_scores()
            elif choice == "3":
                if self.logout():
                    return
            else:
                print(" Oops! This is an invalid choice. Kindly try again.")
                time.sleep(1)
