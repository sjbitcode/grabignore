import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IGNORES_FILE = os.path.join(BASE_DIR, 'ignores.json')

OWNER, REPO = 'github', 'gitignore'
URL = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/'
