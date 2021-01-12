import sys

def main(argv):
    if (len(argv) <= 1):
        err_msg = "\n\tUsage: " + argv[0] + " <src-dir> <dst-dir>\n"
        sys.exit(err_msg)

argv=sys.argv
main(argv)