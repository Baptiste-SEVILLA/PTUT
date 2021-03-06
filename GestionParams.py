import sys
import getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:", ["file="])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -f <file>')
            sys.exit()
        elif opt in ("-f", "--file"):
            print(arg)


if name == "main":
    main(sys.argv[1:])