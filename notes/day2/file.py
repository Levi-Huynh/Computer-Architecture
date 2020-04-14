# read file, splitout out comments, & whitespace

import sys

if len(sys.argv) != 2:
    print("usage: file.py filename")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename) as f:
        for line in f:

            # ignore commentss
            comment_split = line.split("#")

            # strip out whitespace
            num = comment_split.strip()

            # ignore blank lines
            if num == '':
                continue
            print(num)


except FileNotFoundError:
    print("file not found")
    sys.exit(2)
