#Advent of code day 3

import sys


def main():
    inNum = sys.argv[1]
    num = int(inNum)
    puzzleWidth = circleRing(num)
    



def circleRing(num):
    puzzleWidth = 0
    #1, 8, 16, 24, 32, 40 
    #1
    # 3*2 + (3-2) *2  10 + 6   14 + 10  18 + 14  22 + 18 
    # num -1           11
    # num // 8         1
    # ring + 1         2
    # num % 


    return puzzleWidth

