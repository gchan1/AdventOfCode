#Day 2 checksum implementation
import sys

def main():
    print checksum()
    print  evenDivides()

def checksum():
    checksum = 0
    inFile = open(sys.argv[1], 'r')
    for line in inFile:
        numbers = line.strip().split()
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        checksum +=  (max(numbers) - min(numbers))
    inFile.close()
    return  checksum

def evenDivides():
    checksum = 0
    inFile = open(sys.argv[1], 'r')
    for line in inFile:
        numbers = line.strip().split()
        for number1 in numbers:
            for number2 in numbers:
                if number1 != number2 and int(number2) % int(number1) == 0:
                    checksum += (int(number2) / int( number1))
    inFile.close()
    return  checksum
main()
