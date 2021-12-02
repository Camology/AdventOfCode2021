increaseCounter = 0
with open('input.txt') as input:
    lines = input.readlines()
previousLine = lines[0]

for line in lines:
    if (int(line) > int(previousLine)):
        increaseCounter+=1
    previousLine = line

print(increaseCounter)

