import sys


def isPalindrome(word):
    word = (str(word)).lower()
    word_rev = word[::-1]
    if word == word_rev:
        return True
    return False


if __name__ == "__main__":
    word = sys.argv[1]
    print(isPalindrome(word))