The first thing we did was clone the git repositories. For this there is clone_git.py file. This requires personal access tokens, which I have saved (ask me). The clone_git.py can be run from app.py.

After a (one year) repo is downloaded, we need to run remove_git.py because the repositories downloaded wont be committed to master branch otherwise. 

Once we commit all the changes so far to the master branch, we can now run merge.sh so that it only considers the latex files from the repositories. merge.sh uses latexpand in order to concatenate all the latex files in a folder, by removing the comments in them as well. Finally we will have all the publications in Merged folder (careful with merge.sh as it can delete the folder, if path is not correct it will delete without the output file we require). 

Now we use searchtex.py in order to search for various parameters in each of the publications. The code is properly commented. It returns a list in which all the years' publications' parameters are stored in a dictionary. 


