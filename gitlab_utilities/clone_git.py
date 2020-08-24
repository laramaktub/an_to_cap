#https://python-gitlab.readthedocs.io/en/stable/api-usage.html
#https://docs.python.org/2/library/urlparse.html

import gitlab


from urllib.parse import urlparse
from git import Repo

def extract_repos(url, token):
    gl = gitlab.Gitlab(url, token, pagination="keyset", order_by="id", per_page=100)  #To connect to a GitLab server, create a gitlab.Gitlab object
    #return gl
    counter = 0

    for i in gl.groups.list(all=True):
        #print(i.id)
        if i.id == 16803: # id of the group list (Clone only the particular repo)
            projectLists = i.projects.list(all = True) # Use the all parameter to get all the items when using listing methods:
            #print(len(projectLists))
            for project in projectLists:
                url_to_clone = project.http_url_to_repo
                parsedurl = urlparse(url_to_clone)
                path = parsedurl.path
                splitted_path = path.split('/')
                contain_AN = splitted_path[-1]
                splitted_git = contain_AN.split('.')
                valid_git_dir = splitted_git[0]
                full_dir = f'gitTest/{valid_git_dir}'
                print(path)
                print("full dir --> ", full_dir)
                if not full_dir in path:
                    if 'AN-17' in path: #if AN-12 in path, then clone

                        try:
                            Repo.clone_from(url_to_clone, full_dir)
                            counter +=1
                            print(f"completed repos: {counter}")
                        except:
                            print("Skipped path " + path)
    print('Cloning complete')