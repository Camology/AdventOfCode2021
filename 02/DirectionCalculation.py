depth = 0
horizontal = 0
with open('input.txt') as input:
    lines = input.readlines()

for line in lines:
    splitLine = line.split()
    if (splitLine[0] == 'forward'):
        horizontal+=int(splitLine[1])
    elif(splitLine[0] == 'down'):
        depth+=int(splitLine[1])
    elif(splitLine[0] == 'up'):
        depth-=int(splitLine[1])
    else:
        print('bad input')
print(depth*horizontal)