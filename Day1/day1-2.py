file1 = open('input1.txt', 'r')
Lines = file1.readlines()
Lines = [line.rstrip() for line in Lines]


count = 0

for i in range (3, len(Lines)):
    prevWindow = int(Lines[i-1]) + int(Lines[i-2]) + int(Lines[i-3])
    nextWindow = int(Lines[i]) + int(Lines[i-1]) + int(Lines[i-2]) 
    if int(prevWindow) < int(nextWindow):
        count += 1

    
print(count)
##print(nextWindow)
##print(prevWindow)

