import os

def list_items(dir_path):
    with os.scandir(dir_path) as entries:
        for entry in entries:
            print(entry.name, end='')
            if entry.is_dir():
                print("/")
            else:
                print("")