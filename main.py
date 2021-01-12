import sys
import rsync_algorithm as rsync

def main(argv):
    if (len(argv) <= 1):
        err_msg = "\n\tUsage: " + argv[0] + " <src-dir> <dst-dir>\n"
        sys.exit(err_msg)
    rsync.rsync()

argv=sys.argv
main(argv)