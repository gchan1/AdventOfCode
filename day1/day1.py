#this is the reverse captcha problem for day 1
import sys

def main():
    inFile = open(sys.argv[1], "r")
    data = inFile.readlines()
    csums = []
    hsums = []
    for number in data:
        number = number.strip();
        tempSum = addConsecutiveNumbers(number)
        csums.append([number, tempSum])
        print("Consecutive sum: " , tempSum)
        tempSum = addHalfRoundNumbers(number)
        hsums.append([number, tempSum])
        print("HalfRound sum: ", tempSum)

def addConsecutiveNumbers(number):
    sum = 0
    for i in range(len(number)):
        if number[i] == number[i-1]:
            sum += int(number[i])
    return sum

def addHalfRoundNumbers(number):
    sum = 0
    for i in range(len(number)):
        halfRound = (i + (len(number)//2)) % len(number)
        if number[i] == number[halfRound]:
            sum += int(number[i])
    return sum

main()
