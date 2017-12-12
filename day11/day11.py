#day 11 advent of code 2017

import sys
import math


def distance(data):
    deltas = [0,0,0]
    distances = []
    steps = {
        'n': [0,1],
        's': [0, -1],
        'ne': [1,-1],
        'sw': [1,1],
        'nw': [2,1],
        'se': [2, -1]
        }
    for val in data:
        if val not in steps.keys():
            return "ERROR"
        tempVal = steps[val]
        deltas[tempVal[0]] += tempVal[1]
        distances.append(abs(deltas[0]) + max(abs(deltas[1]),abs(deltas[2])))

    for num in deltas:
        num = abs(num)

    dist = (abs(deltas[0]) + max(abs(deltas[1]),abs(deltas[2])))
    print "Shortest distance to child: " + str(dist)
    print "Farthest the child was from home: "  + str(max(distances))

def main():
    inFile = open(sys.argv[1], 'r')
    data = inFile.readline().strip().split(',')
    distance(data)

main()
