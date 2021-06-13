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
        items_copy = os.scandir(self.dir_path) #cloning self.items
        dirs = []
        for entry in items_copy:
            print("dir:")
            if entry.is_dir():
                dirs.append(entry) #append() modifies original list
        return dirs

    def getDirSize(self, dir_path, size=0):
        temp_dir = self.dir_path + dir_path
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_file():
                    # print(entry.name, ", ",end='', sep='')
                    # print(os.stat(entry).st_size)
                    size += os.stat(entry).st_size
                else:
                    print ('\t', (dir_path + entry.name + '/'))
                    size = self.getDirSize((dir_path + entry.name + '/'), size)
        return size