# -*- coding: utf-8 -*-
# Python 3
# This is a sample Python script to validate incoming FLAC music files
# and change (if reaquired) before adding to main music library
#
# python3 checkmusicfiles.py C:\\Users\\jon_a\\Music

import os
import json

# fastest method to scan directories recursively
def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files

if __name__ == '__main__':
   # read the rules file, import transformation rules
   

   # Directory to be scanned
   folder = '/home/jon/Music'
   subfolders, files = run_fast_scandir(folder, [".flac"])

   # https://www.geeksforgeeks.org/python-string-translate/
   # load the translation rules from config.ini
   table = str.maketrans('aeiou', '12345')
   # load blank rulesimport json


    # run all required routines to check / change files as required

    # STEP 1 - rename if necessary
   for filename in files:
        # file names
        # print(filename)
        # just the filename
        filename_= os.path.basename(filename)
        # print(filename)
        # translated
        print(filename.translate(table))
