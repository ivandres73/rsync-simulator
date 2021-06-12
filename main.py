import sys
import rsync_algorithm as rsync

def main(argv):
    if (len(argv) <= 2):
        err_msg = "\n\tUsage: " + argv[0] + " <src-dir> <dst-dir>\n"
        sys.exit(err_msg)
    source = argv[1]
    destin = argv[2]
    if not(source.endswith('/')):
        source = source + "/"
    if not(destin.endswith('/')):
        destin = destin + "/"
    rsync.rsync(source, destin)

# ENTRY POINT
main ( sys.argv )