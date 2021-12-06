inputFile = open('input.txt', 'r')
instructions = inputFile.readlines()
instructions = [instruction.rstrip() for instruction in instructions]
oxygenArray = []
coArray = []

oxygenNums = instructions.copy()
coNums = instructions.copy()
  
def removeNum(numToRemove, col, workingList):
    for instruction in workingList[:]:
        if (int(instruction[col]) == numToRemove) and len(workingList) > 1:
            workingList.remove(instruction)


def getO2(col):
    for instruction in oxygenNums: # for each row
        # Look at the bit in current (col) column. append digit to list
        oxygenArray.append(int(instruction[col])) 

    if oxygenArray.count(0) <= oxygenArray.count(1):
        removeNum(0, col, oxygenNums)
    else:
        removeNum(1, col, oxygenNums)

    oxygenArray.clear()

def getCO2(col):
    for instruction in coNums: # for each row
        # Look at the bit in current (col) column. append digit to list
        coArray.append(int(instruction[col])) 

    if coArray.count(0) <= coArray.count(1):
        removeNum(1, col, coNums)
    else:
        removeNum(0, col, coNums)

    coArray.clear()

def getLifeSupport():
    for col in range(0, 12): # for each column
        getO2(col)
        getCO2(col)

getLifeSupport()
    
o2Dec = (int(oxygenNums[0], 2)) # convert from binary to decimal
co2Dec = (int(coNums[0], 2)) # convert from binary to decimal

print(f'O2 gen rating: {o2Dec} CO2 gen rating {co2Dec}')
print(co2Dec*o2Dec) # Answer is o2 gen rating * CO2 gen rating 
