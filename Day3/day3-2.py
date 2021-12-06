inputFile = open('/home/colin/Documents/scratch/adventOfCode/AdventOfCode/Day3/testinput.txt', 'r')
instructions = inputFile.readlines()
instructions = [instruction.rstrip() for instruction in instructions]
numArray = []



'''
    Get the most common value for the first bit
'''
def getFirstBits():
    for i in range(0, 5): # for each column
        for instruction in instructions: # for each row
            numArray.append(int(instruction[i]))
        if numArray.count(0) > numArray.count(1):
            removeNum(0)
        else:
            removeNum(1)

def removeNum(numToRemove):
    for instruction in instructions:
        if instruction.startswith(str(numToRemove)):
            instructions.remove(instruction)
     
getFirstBits()     

print(instructions)


#print(numArray.count(0))
#print(numArray.count(1))

#def getOxygenRating():


#val = getFirstBits()
#outputArray = []
#def oxygenRating(val):
#    for instruction in instructions:
#        if instruction.startswith(str(val)):
#                outputArray.append(instruction)
#    print(outputArray)
#oxygenRating(val)
