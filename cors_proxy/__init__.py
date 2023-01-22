from proxy import *


def main():
    if (len(argv) == 3):
        (path, host, port) = argv
        proxy(host, int(port)).listen()

    else:
        print(__doc__)


main()
