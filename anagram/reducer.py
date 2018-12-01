import sys


def reducer():
    current_word = None
    word = None
    current_array = []
    for line in sys.stdin:
        current_word, value = line.split("\t")
        value=value.strip()
        if current_word == word:
            current_array.append(value)
        else:
            print(word, current_array)
            if current_word:
                current_array = []
                word = current_word
                current_array.append(value)

    print(word, current_array)
    current_array = []


reducer()
