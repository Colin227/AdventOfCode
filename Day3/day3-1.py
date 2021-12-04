
inputFile = open('input.txt', 'r')
instructions = inputFile.readlines()
instructions = [instruction.rstrip() for instruction in instructions]



def processInput():
    countOne = 0
    countZero = 0


    mostCommon = []
    leastCommon = []
    for i in range(0, 12): # loop through each digit in instruction
        for instruction in instructions: #loop through each instruction[i]
            tmpCount = countValue(instruction[i])
            if tmpCount > 0:
                countOne += 1  
            else:
                countZero += 1
        if countOne > countZero:
                mostCommon.append(1)
                leastCommon.append(0)
        else:
                mostCommon.append(0)
                leastCommon.append(1)
        countOne = 0
        countZero = 0
        #print(countOne, countZero)
    print(mostCommon, leastCommon)

def countValue(currentValue):
    if int(currentValue) == 1:
        return 1
    else: return 0
processInput()
