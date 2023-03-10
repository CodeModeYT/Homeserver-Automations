# THIS SCRIPT IS USED TO SYNCHRONIZE THE DATA FROM MY MAIN SERVER TO MY BACKUP SERVER

import os
import shutil

source = "M:/"
destination = "Z:/"

def copy_files(src, dst):
    try:
        shutil.copy2(src, dst)
    except PermissionError:
        print(f"Skipping {src} due to a permission error.")
        pass

def start():
    for root, dirs, files in os.walk(source):
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(destination, os.path.relpath(src_path, source))
            copy_files(src_path, dst_path)


start()
print("Successfully backed up your files from your NAS to the MyCloud!")

