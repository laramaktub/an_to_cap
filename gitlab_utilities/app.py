import os

from gitlab_utilities.clone_git import extract_repos

#url = 'https://gitlab.cern.ch'
url = 'https://gitlab.cern.ch'

token = os.getenv('GITLAB_TOKEN')

if __name__ == '__main__':
    extract_repos(url, token)
    print("completed extraction of repos")