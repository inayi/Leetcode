#!/usr/bin/env python3

# 917. Reverse Only Letters
# Given a string S, return the "reversed" string
# All characters that are not a letter stay in the same place.
# All letters reverse their positions.

def reverseOnlyletter(string):
    letters = [c for c in string if c.isalpha()]
    reversed = []
    for c in string:
        if c.isalpha():
            reversed.append(letters.pop())
        else:
            reversed.append(c)
    return ''.join(reversed)

if __name__ == "__main__":
    test = reverseOnlyletter("Test1ng-Leet=code-Q!")
    print(test)
    # should be "Qedo1ct-eeLg=ntse-T!"

