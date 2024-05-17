# score.py
from datetime import datetime
from util.user import User

class Score:
    def __init__(self, player_user, session_id, total_points=0, total_wins=0):
        self.player_name = player_user
        self.session_id = session_id
        self.total_points = total_points
        self.total_wins = total_wins
    
    def update_score(self, points_earned, wins_earned):
        self.total_points += points_earned
        self.total_wins += wins_earned
    
    def reset_current_score(self):
        return 0, 0

    def reset_all_scores(self):
        self.total_points = 0
        self.total_wins = 0
    
    def to_record(self):
        self.session_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.player_name, self.total_points, self.total_wins, self.session_id
