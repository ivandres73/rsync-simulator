import dir_analyzer as da

def rsync(source, destin):
    d1 = da.Directory(source)
    print(d1.getName())
    src_dirs = d1.getDirs()
    for i in src_dirs:
        print(d1.getDirSize(source + i.name + '/'))
    total = d1.getDirSize(d1.getName())
    print("d1 total =", total)
    print("--------------")
    # printing for 2nd directory
    d2 = da.Directory(destin)
    print(d2.getName())
    dst_dirs = d2.getDirs()
    for j in dst_dirs:
        print(d2.getDirSize(destin + j.name + '/'))
    total = d2.getDirSize(d2.getName())
    print("d2 total =", total)
    # check if same size to avoid any processing
    if ( d1.getDirSize(d1.getName()) == d2.getDirSize(d2.getName()) ):
        print("\n\tthere are no files to update, aborting...")
        return

    # sizes aren't the same, check which ones
    for s_dir in src_dirs:
        for d_dir in dst_dirs:
            if s_dir.name == d_dir.name:
                src_absolute_name = source + s_dir.name + '/'
                dst_absolute_name = destin + d_dir.name + '/'
                if d1.getDirSize(src_absolute_name) != d2.getDirSize(dst_absolute_name):
                    print(s_dir.name, " has not same size as", d_dir.name) # process which files/dirs are different

def rsync_update_dst_dir(sour, dest):
    ## validate if file is in destin

    ## validate if file doesn't exist at all in destin

    ## validate if directory is in destin (do a recursive call)

    ## validate if directory doesnt exist at all in destin
    for s_dir in src_dirs:
        for d_dir in dst_dirs:
            if s_dir.name == d_dir.name:
                src_absolute_name = source + s_dir.name + '/'
                dst_absolute_name = destin + d_dir.name + '/'
                if d1.getDirSize(src_absolute_name) != d2.getDirSize(dst_absolute_name):
                    print(s_dir.name, " has not same size as", d_dir.name) # process which files/dirs are different