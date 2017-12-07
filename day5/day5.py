#advent of code day 5

import sys

def main():
    inFile = open(sys.argv[1], 'r')
    maze = []
    for line in inFile:
        maze.append(int(line.strip()))
    mazeLen = len(maze)
    ind = 0
    steps = 0
    while ind >= 0 and ind < mazeLen:
       steps += 1
       newInd = ind + maze[ind]
       if maze[ind] >= 3:
           maze[ind] -= 1
       else:
           maze[ind] += 1
       ind = newInd
    print steps
main()
