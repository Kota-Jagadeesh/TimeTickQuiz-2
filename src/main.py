# main file to run timetickquiz-2 pro
from user_profile import UserProfile
from quiz_engine import QuizEngine
from rich.console import Console
from utils import get_categories

console = Console()

def main():
    console.print("[bold blue]welcome to timetickquiz pro![/bold blue]")
    # write u r code here to:
    # - prompt for username
    # - create user profile
    # - get quiz settings (num questions, difficulty, time limit)
    # - show categories and let user pick one
    # - start the quiz

if __name__ == "__main__":
    main()