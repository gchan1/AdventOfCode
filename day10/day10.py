#day 10 of advent of code
import sys

def main():
    inFile = open(sys.argv[1], 'r')
    moves = inFile.readline().strip().split(',')

    origArray = buildArray(256)
    newArray = tieKnots(origArray, moves)
    print newArray[0] * newArray[1]
    
def buildArray(size):
    numArray = []
    for i in range(size):
        numArray.append(i)
    return numArray

def tieKnots(numList, movesList):
    ind = 0
    step = 0
    numListLen = len(numList)

    while len(movesList) > 0:

        move = int(movesList[0])
        endInd = ind + move

        if endInd >= numListLen:

            subList = numList[ind:]
            endInd = endInd % numListLen
            subList.extend(numList[0:endInd])
            subList.reverse()            
            tempI = 0

            for i in range(ind, numListLen):
                numList[i] = subList[tempI]
                tempI += 1
            for j in range(endInd):
                numList[j] = subList[tempI]
                tempI += 1
        else:
            subList = numList[ind:endInd]
            subList.reverse()
            tempI = 0
            for i in range(ind, endInd):
                numList[i] = subList[tempI]
                tempI += 1

        ind = ind + move + step
        ind = ind % numListLen
        step += 1
        movesList.pop(0)
    
    return numList
        

main()
