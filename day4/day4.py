#advent of code day 4

import sys

def main():
    valid = 0
    inFile = open(sys.argv[1], 'r')
    for line in inFile:
        line = line.strip().split()
        words = []
        for word in line:
            word = word.strip()
            word = list(word)
            word.sort()
            if word not in words:
                words.append(word)
            else:
                break
        if len(words) == len(line):
            valid += 1


    print valid
    
main()
