import sys

memory = [None] * 256
register = [0] * 8
pc = 0

running = True


def load_memory(filename):
    address = 0
    try:
        with open(filename) as f:
            for line in f:

                # ignore commentss
                comment_split = line.split("#")

            # strip out whitespace
                num = comment_split[0].strip()

            # ignore blank lines
                if num == '':
                    continue
                    print(num)

                val = int(num)
                memory[address] = val
                address += 1

    except FileNotFoundError:
        print("file not found")
        sys.exit(2)


if len(sys.argv) != 2:
    print("usage: simple.py filename")
    sys.exit(1)

filename = sys.argv[1]
