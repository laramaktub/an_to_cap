from pathlib import Path
import os
import glob
import re
main_list = []
pattern  = re.compile("[^a-zA-Z0-9_]") #Takes alphanumeric only
def return_params(mainFolderLocation):

    #https://www.tutorialspoint.com/python/os_walk.htm
    for subdir, dirs, files in os.walk(mainFolderLocation):
        tem_dict = {}
        for file in files:  # Lets iterate through all the merged files
            temp_main_root = f'{subdir}'  # Current Folder
            # check all .tex file from folder and read them:
            search_params = {}  # Dicitionary
            data = []
            temp_dataset = []  # Dataset
            trigger = []
            version = []
            mc = []  # Monte Carlo
            git_repo = []
            globalTag = []

            output_merged_file = f'{temp_main_root}/{file}'

                # check all .tex file from folder and read them:
            with open(output_merged_file, encoding='latin-1') as temp_file:
                for line in temp_file:
                    #print (line,)

                    #Updated search primary dataset
                    ''' This will search for all the lines ending in /AOD, /MINIAOD ...'''
                    if('/AOD' in line or '/MINIAOD' in line or '/NANOAOD' in line or '/RECO' in line):
                        lst = ([word for word in line.split(' ')])
                        for word in lst:
                            st = re.match(r"^\/.*\/AOD$",word) # We do strict matching (ending in AOD) otherwise it can capture AODSIM as well.
                            #print(st)
                            if st is not None:
                                #print(st.group(0))
                                data.append(st.group(0))

                    #For trigger we give this condition
                    if ('HLT_' in line or 'hlt_' in line):
                        # line=line.split(' ')
                        for word in line.split(' '):
                            if word.startswith('HLT{\\_}'):
                                a = pattern.sub('', word)
                                trigger.append(a)

                    #For software version, we give this condition
                    if ('CMSSW' in line):
                        for cmssw in line.split(' '):
                            if cmssw.startswith('CMSSW\\'):
                                a = pattern.sub('', cmssw)
                                version.append(a)
                        #If there are more than one software versoi
                        if len(version) > 1:
                            line = line.split('.')
                            # print(line)
                            for l in line:
                                if 'CMSSW' in l:
                                    version.append(l)
                        # if 'global tag' in x or 'gt' = x or 'GT' in x or 'globaltag' in x:
                        #     globalTag.append(x)
                '''For each directory (dir) or the main mergedlatex files, do the dictionary operations '''
            search_params['data'] = data
            search_params['trigger'] = trigger
            search_params['version'] = version
            search_params['mc'] = mc
            #search_params['git_repo'] = dir  # if needed we can enter gitlab links
            search_params['global_tag'] = globalTag


            tem_dict[file] = search_params

        for di in tem_dict.items():
            # print(di[0]) #Name of dictionary
            for item in (di[1].items()):
                # print(item[1])
                if (len(item[1]) > 0):
                    print(di[0], 'has ', item[0])

        main_list.append(tem_dict)  # This is out of the for dir in dirs so that it wont overwrite
        # next(array for key, array in tem_dict.items() if array)
        # non_empty = len([array for key, array in tem_dict.items() if array])
        # empty = len([array for key, array in tem_dict.items() if not array])
        return (main_list)


data = return_params('Merged')
print(data)
