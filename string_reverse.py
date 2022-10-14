"""
Author: Vishnu M J
Task: Reverse each word in the input string without reversing the special characters.
"""


def reverse_each_word(sentence):
    wd = ""
    rev = ""
    for ch in sentence:
        if ch.isalnum():
            wd = wd + ch
        else:
            rev = f"{rev}{wd[::-1]}{ch}"
            wd = ""

    rev = f"{rev}{wd[::-1]}"

    return rev


if __name__ == '__main__':
    test_str = "Stri_ng;-%   2b$#e reversed"
    rev_str = reverse_each_word(test_str)
    print(rev_str)

    assert rev_str == "irtS_gn;-%   b2$#e desrever"

