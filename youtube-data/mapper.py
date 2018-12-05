import sys


"""
This uses the file youtubedata and counts the videos whenever each categories is encountered
key,value:
categories,1
"""

def mapper():
    for line in sys.stdin:
        line = line.strip()
        line = line.split("\t")
        if len(line) < 10:
            continue
        try:
            print(line[3], 1, sep=",")
        except IndexError:
            print("index","1",line[0],sep='1')

mapper()
