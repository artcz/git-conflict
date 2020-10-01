from sys import exit


def count(start, end, interval):
    while start < end:
        yield start
        start += interval


def count2(start, end, interval):
    numbers = []
    for i in range(start, end, interval):
        numbers.append(i)

    return numbers


def main():
    cc = count(1, 1337, 21)
    for c in cc:
        print(c)

    return 0


if __name__ == '__main__':
    exit(main())
