#advent of code day 6

import sys

def part1(data):
    states = []
    state = data
    steps = 0
    while state not in states:
        steps += 1
        tempState = list(state)
        maxInd = tempState.index(max(state))
        maxVal = (max(tempState))
        tempState[maxInd] = 0
        for i in range(maxVal):
            curInd = (maxInd + i + 1) % len(state)
            tempState[curInd] += 1
        states.append(state)
        state = tempState
    print("steps until duplicate: " + str(steps))

def part2(data):
    states = []
    seen = []
    saveState = []
    state = data
    steps = 0

    while states.count(state) < 2:
        steps += 1
        tempState = list(state)
        maxInd = tempState.index(max(state))
        maxVal = (max(tempState))
        tempState[maxInd] = 0

        for i in range(maxVal):
            curInd = (maxInd + i + 1) % len(state)
            tempState[curInd] += 1

        if tempState == saveState:
            seen.append(steps)
        if tempState in states and saveState == []: 
            seen.append(steps)
            saveState = list(tempState)
        states.append(state)
        state = tempState
    print("steps between first duplicate and next occurance: " + str(seen[1] - seen [0]))

def main():
    inFile = open(sys.argv[1], 'r')
    data = inFile.readline().strip().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    part1(data)
    part2(data)

main()
