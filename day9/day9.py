#advent of code day 9

import sys

def main():
    inFile = open(sys.argv[1], 'r')
    data = list(inFile.readline().strip())

    level = 0
    score = []
    inGarbage = False
    garbage = []
    brack = []
    no = 0
    dataLen = len(data)
    for i in range(dataLen):
        char = data[i]
        
        if inGarbage == False:
            if char == '<':
                inGarbage = True
                continue
            elif char == '{':
                level += 1
                score.append(level)
            elif char == '}' and data[i-1] != '!':
                level -= 1
        
        else:
            if data[i-1] == '!':
                if char == '!' :
                    data[i] = ''
                    data[i-1] = ''
            else:
                if char == '>':
                    inGarbage = False
                elif char != '!':
                    garbage.append(char)

    print 'Score: ' + str(sum(score))
    print 'Size of Garbage: ' + str(len(garbage))

main()
