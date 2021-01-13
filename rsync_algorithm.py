import dir_analyzer as da

def rsync(source, destin):
    print("reventuki")
    da.list_items(source)
    d1 = da.Directory(source)
    print(d1.getName())
    # print(d1.getDirs())
    d1.getDirSize('.git/')