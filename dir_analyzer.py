import os

def list_files(dir_path):
    with os.scandir(dir_path) as entries:
        for entry in entries:
            print(entry.name)