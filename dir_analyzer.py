import os

def list_items(dir_path):
    with os.scandir(dir_path) as entries:
        for entry in entries:
            print(entry.name, end='')
            if entry.is_dir():
                print("/")
            else:
                print("")

class Directory:
    def __init__(self, dir_path):
        self.items = os.scandir(dir_path)
        self.dir_path = dir_path

    def getName(self):
        return self.dir_path

    def getDirs(self):
        dirs = []
        with self.items as entries:
            for entry in entries:
                if entry.is_dir():
                    dirs.append(entry)
        return dirs

    def getDirSize(self, dir_path, size=0):
        temp_dir = self.dir_path + dir_path
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_file():
                    size += os.stat(entry).st_size
                else:
                    size = self.getDirSize((dir_path + entry.name + '/'), size)
        return size