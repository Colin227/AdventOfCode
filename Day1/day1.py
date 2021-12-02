file1 = open('input1.txt', 'r')
Lines = file1.readlines()
Lines = [line.rstrip() for line in Lines]


count = 0

for i in range (1, len(Lines)):
    if (int(Lines[i]) > int(Lines[i-1])):
        count += 1     

print(count)
