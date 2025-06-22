# utility functions for quiz
import json
import os
import requests

PROFILE_FILE = os.path.join(os.path.dirname(__file__), '../profiles.json')
CATEGORY_URL = "https://opentdb.com/api_category.php"

def load_profiles():
    # write u r code here to:
    # - load profiles from profiles.json
    # - return profiles list

def save_profiles(profiles):
    # write u r code here to:
    # - save profiles to profiles.json

def get_profile(username):
    # write u r code here to:
    # - find profile by username
    # - return profile or None

def update_profile(new_profile):
    # write u r code here to:
    # - update or add profile to profiles.json

def get_categories():
    # write u r code here to:
    # - fetch categories from CATEGORY_URL
    # - handle errors and return categories list