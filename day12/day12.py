#advent of code day 12
import sys

def main():
    inFile = open(sys.argv[1],'r')
    numGroups = 0
    pipeDic = dict()

    for line in inFile:
        line = line.strip().split('<->')
        pipe = line[0].strip()
        conn = line[1].split(', ')
        pipeDic[pipe] = conn

    pipeQ = ['0']
    first = 0
    pipesInvolved = []

    while len(pipeDic.keys()) > 0:

        #Get the pipe network starting at the first in Q
        while len(pipeQ) > 0:
            cur = pipeQ[0].strip()
            curChild = pipeDic[cur]
            if cur not in pipesInvolved:
                pipeQ.extend(curChild)
                pipesInvolved.append(cur)
            pipeQ.pop(0)    
            
        #Print the number of pipes for part 1
        if first == 0:
            print len(pipesInvolved)
            first = 1

        #Additions to basic algorithm for part 2
        for pipe in pipesInvolved:
            pipeDic.pop(pipe)

        pipesInvolved = []
        numGroups += 1
        if len(pipeDic.keys()) > 0:
            pipeQ = [pipeDic.keys()[0]]
    
    print numGroups

main()
