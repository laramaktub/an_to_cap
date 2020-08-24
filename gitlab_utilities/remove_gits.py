import glob
import os

def set_rw(operation, name, exc):
    os.chmod(name, stat.S_IWRITE)
    return True

main_list = []
main_folder = 'gitTest'
#walk() generates the file names in a directory tree by walking the tree. gitTest\AN-...\*.*
for dirname, dirs, files in os.walk(main_folder):
    tem_dict = {}
    for dir in dirs:
        temp_main_root = f'{dirname}/{dir}'  #Folder AN-....

        extra_level = {} # Dicitionary
        temp_data_set = [] #Dataset
        trigger = []
        version = []
        mc = [] #Monte Carlo
        git_repo = []
        globalTag = []
        # *.tex files
        import shutil
        import stat
        import subprocess
        for files in os.listdir(temp_main_root):
            if files == '.git':
                # for file in os.listdir(f'{temp_main_root}/{files}'):
                os.chmod(f'{temp_main_root}/{files}', stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
                shutil.rmtree(f'{temp_main_root}/{files}', onerror=set_rw)
                print(f"deleted {files}")


