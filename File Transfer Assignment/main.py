import shutil
import os

source = '/Users/atulo/Desktop/Folder-A/'

destination = '/Users/atulo/Desktop/Folder-B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)

    
