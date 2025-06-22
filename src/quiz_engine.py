# handles quiz logic and api calls
import requests
import html
import threading
import time
from rich.console import Console

console = Console()
CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"

class QuizEngine:
    def __init__(self, profile, num_questions, difficulty, time_limit, category_id):
        self.profile = profile
        self.num_questions = num_questions
        self.difficulty = difficulty
        self.time_limit = time_limit
        self.category_id = category_id
        self.questions = []
        self.score = profile.score

    def fetch_questions(self):
        # write u r code here to:
        # - build params for api call
        # - fetch questions from QUESTION_URL
        # - handle errors and store questions

    def ask_question(self, question_data):
        # write u r code here to:
        # - decode question and answers
        # - show question and options
        # - use threading to enforce time limit
        # - get user input and check if correct
        # - return True for correct, False for incorrect

    def run(self):
        # write u r code here to:
        # - fetch questions
        # - loop through questions and ask them
        # - update score and show final results