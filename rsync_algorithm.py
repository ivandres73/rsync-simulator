import dir_analyzer as da

def rsync(source, destin):
    d1 = da.Directory(source)
    print(d1.getName())
    src_dirs = d1.getDirs()
    print(src_dirs)
    for i in src_dirs:
        print(d1.getDirSize(i.name + '/'))
    # total = d1.getDirSize('prueba/')
    # print("total =", total)