import os
import shutil
import pandas as pd

path = (r'D:\MASTERS\pyth\Project3\\')

folder_names = ['CSV files', 'PNG files', 'Text Files', 'JSON files', 'Excel Files']

for folders in folder_names:
    if not os.path.exists(path + folders):
        os.mkdir(path + folders)

file_names = os.listdir(path)

for files in file_names:
    if '.csv' in files and not os.path.exists(path + 'CSV files' + files):
        shutil.move(path + files, path + 'CSV files\\' + files)
    elif '.png' in files and not os.path.exists(path + 'PNG files' + files):
        shutil.move(path + files, path + 'PNG files\\' + files)
    elif '.txt' in files and not os.path.exists(path + 'Text files' + files):
        shutil.move(path + files, path + 'Text files\\' + files)
    elif '.json' in files and not os.path.exists(path + 'Text files' + files):
        shutil.move(path + files, path + 'JSON files\\' + files)
    elif '.xlsx' in files and not os.path.exists(path + 'Text files' + files):
        shutil.move(path + files, path + 'Excel files\\' + files)
