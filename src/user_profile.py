# manages user profiles
from utils import get_profile, update_profile

class UserProfile:
    def __init__(self, username):
        # write u r code here to:
        # - load existing profile or create new one
        # - set username, score, high score, difficulty

    def increase_score(self):
        # write u r code here to:
        # - increase score
        # - update high score if needed
        # - adapt difficulty based on score
        # - save profile

    def adapt_difficulty(self):
        # write u r code here to:
        # - adjust difficulty based on score (e.g., hard if score > 50)

    def save(self):
        # write u r code here to:
        # - save profile to profiles.json