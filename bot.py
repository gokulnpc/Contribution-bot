import os
import subprocess
from datetime import datetime

# Load the GitHub token from the environment variable
github_token = os.getenv('GITHUB_TOKEN')

def configure_git():
    # Configure Git with user name and email
    subprocess.run(['git', 'config', '--global', 'user.email', 'gokulnpc@gmail.com'], check=True)
    subprocess.run(['git', 'config', '--global', 'user.name', 'gokulnpc'], check=True)

def make_commit():
    # Update a file
    file_path = os.path.join(os.path.dirname(__file__), 'daily_update.txt')
    with open(file_path, 'a') as file:
        file.write(f'Update on {datetime.now()}\n')

    try:
        # Fetch repository URL
        remote = subprocess.run(['git', 'remote', '-v'], check=True, capture_output=True, text=True)
        print(f'Repository URL: {remote.stdout}')

        # Git operations
        subprocess.run(['git', 'add', './*'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Daily update'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Failed to commit and push changes: {e}')

if __name__ == '__main__':
    configure_git()
    make_commit()
