import sys


def reducer():
    current_word = None
    word = None
    current_array = []
    for line in sys.stdin:
        current_word, value = line.split("\t")
        value=value.strip()
        #if there is no change of key keep on appending to the list of anagram array
        if current_word == word:
            current_array.append(value)
        else:
            #if the key is changed print the previous anagram list
            #and empty the array
            res=" ".join(current_array)
            if(len(current_array)>1):
                res=" ".join(current_array)
                print(res)
            if current_word:
                current_array = []
                word = current_word
                current_array.append(value)

    if(len(current_array)>1):
        res=" ".join(current_array)
        print(res)
    current_array = []


reducer()
