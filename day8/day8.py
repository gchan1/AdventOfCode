#advent of code day 8

import sys

def main():
    registers = dict()
    incDec = {
        'inc' : 1,
        'dec' : -1
        }
    allVals = []
    inFile = open(sys.argv[1], 'r')
    for line in inFile:
        line = line.strip().split('if')
        stmt = line[1].strip().split()
        if stmt[0] not in registers.keys():
            registers[stmt[0]] = 0
        stmt = 'registers[\'' + stmt[0] + '\'] ' + stmt[1] + ' ' + stmt[2]
        direc = line[0].split()
        reg = direc[0]
        id = direc[1]
        val = int(direc[2])
        if reg not in registers.keys():
            registers[reg] = 0
        if eval(stmt):
            registers[reg] += (incDec[id] * val)
            allVals.append(registers[reg])
    print max(registers.values())
    print max(allVals)
main()
