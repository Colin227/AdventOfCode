# currentPosition = [horizontal, depth]
horizontal = 0
depth = 0


instructionsFile = open('input.txt', 'r')
instructions = instructionsFile.readlines()
instructions = [instruction.rstrip() for instruction in instructions]

for i in range(0, len(instructions)):
    if (instructions[i].startswith('forward')):
        horizontal = horizontal + int(instructions[i][-1])
    if (instructions[i].startswith('down')):
        depth = depth + int(instructions[i][-1])
    if (instructions[i].startswith('up')):
        print(int(instructions[i][-1]))
        depth = depth - int(instructions[i][-1])

currentPosition = [horizontal, depth]
print(currentPosition)
print(horizontal * depth) # this is the answer needed
        