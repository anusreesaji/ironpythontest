import sys


def isOdd(number):
    if number % 2:
        return True
    return False


if __name__ == "__main__":
    num = int(sys.argv[1])
    print(isOdd(num))
