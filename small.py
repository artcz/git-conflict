from sys import exit
import itertools


def count(start, end, interval):
    while start < end:
        yield start
        start += interval


def count3(start, end, interval):
    counter = itertools.count(start, interval)

    for c in counter:
        if c >= end:
            break

        yield c


def main():
    cc = count(1, 1337, 21)
    for c in cc:
        print(c)

    return 0


if __name__ == '__main__':
    exit(main())
