
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
            if int(instruction[i]): # If value is 1 this evaluates as true
                countOne += 1  
            else:
                countZero += 1
                
        # Compare number of 0's and 1's, append most/least common value to appropriate array
        if countOne > countZero: 
                mostCommon.append(1)
                leastCommon.append(0)
        else:
                mostCommon.append(0)
                leastCommon.append(1)
        
        # reset counter before moving to next index
        countOne = 0
        countZero = 0
        #print(countOne, countZero)
    print(mostCommon, leastCommon)

processInput()
