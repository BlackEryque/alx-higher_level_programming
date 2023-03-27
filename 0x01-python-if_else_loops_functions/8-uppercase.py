#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for letter in str:
        numb = ord(letter)
        if (numb >= 97) and (numb <= 122):
            numb -= 32
        print(chr(numb), end="")
    print("\n", end="")
