import sys


def mapper():
    total = 0
    for str_in in sys.stdin:
        str_in = str_in.strip()
        line = ''.join(sorted(str_in))
        print(line, str_in , sep="\t")


mapper()
