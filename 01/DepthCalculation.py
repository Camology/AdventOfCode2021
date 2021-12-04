# increaseCounter = 0
# with open('input.txt') as input:
#     lines = input.readlines()
# previousLine = lines[0]

# for line in lines:
#     if (int(line) > int(previousLine)):
#         increaseCounter+=1
#     previousLine = line

# print(increaseCounter)
# part 2
increaseCounter = 0
position = 0
intList = []
with open('input.txt') as input:
    lines = input.readlines()
    for line in lines:
        intList.append(int(line))
previousSum = sum(intList[position:position+3])
for int in intList:
    if len(intList[position:position+3]) == 3:
        a = sum(intList[position:position+3])
        if (a > previousSum):
            increaseCounter+=1
        previousSum = a
        position+=1
print(increaseCounter)
