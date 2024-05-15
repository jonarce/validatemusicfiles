# -*- coding: utf-8 -*-
# Python 3
# This is a sample Python script to validate incoming FLAC music files
# and change (if reaquired) before adding to main music library

import os

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
    # Directory to be scanned
    folder = '/home/jon/Music'
    subfolders, files = run_fast_scandir(folder, [".flac"])
    # run all required routines to check / change files as required
    for file in files:
        # file names
        print(file)

