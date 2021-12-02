horizontal = 0
depth = 0
aim = 0

instructionsFile = open('input.txt', 'r')
instructions = instructionsFile.readlines()
instructions = [instruction.rstrip() for instruction in instructions]

for i in range(0, len(instructions)):
    x = int(instructions[i][-1])
    if (instructions[i].startswith('forward')):
        horizontal = horizontal + x
        depth = depth + (aim * x)

    if (instructions[i].startswith('down')):
        aim = aim + x
    if (instructions[i].startswith('up')):
        aim = aim - x

currentPosition = [horizontal, depth, aim]
print(currentPosition)
print(horizontal * depth)