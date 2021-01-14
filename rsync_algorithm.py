import dir_analyzer as da

def rsync(source, destin):
    # da.list_items(source)
    d1 = da.Directory(source)
    print(d1.getName())
    # print(d1.getDirs())
    total = d1.getDirSize('prueba/')
    print("total =", total)