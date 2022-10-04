"""
Author: Vishnu M J
Task: Reverse each word in the input string without reversing the special characters.

Logic:
1. Split space separated string into words
2. reverse the word if the word only having alphanumeric
3. if the word having special characters, then trim the word till special character and reverse it and special character
   not reversed
4. reversed word is append to the word_list
5. convert word list to space separated string and return
"""


def reverse_each_word(sentence):
    word_list = []
    for word in sentence.split(' '):
        wd, rev_word = "", ""
        if word.isalnum():
            word_list.append(word[::-1])  # reverse the word if word has only alphanumeric
        else:
            for i, ch in enumerate(word):
                if ch.isalnum():
                    wd = wd + ch  # append the characters till the special character found
                if i == len(word) - 1 or not ch.isalnum():
                    rev_word = rev_word + wd[::-1]  # reverse the current word and append to the rev_word if the special character found or last character
                    if not ch.isalnum():
                        rev_word = rev_word + ch  # append the special character without reversing
                    wd = ""
            word_list.append(rev_word)

    return ' '.join(word_list)


def main():
    test_str = "Stri_ng;-%   2b$#e reversed"
    rev_str = reverse_each_word(test_str)
    print(rev_str)


if __name__ == '__main__':
    main()
