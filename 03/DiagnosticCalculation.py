def calculateRate(input,type):
    rate = []
    rowCounter = 0
    while (rowCounter < len(input[0])):
        columnCounter = 0
        zero = 0
        one = 0
        while columnCounter < len(input):
            for line in input:
                if int(input[columnCounter][rowCounter]) == 0:
                    zero+=1
                elif int(input[columnCounter][rowCounter]) == 1:
                    one+=1
                else: 
                    print('bad input')
                columnCounter+=1
            if (type == 'gamma'):
                rate.append('0') if zero > one else rate.append('1')
            elif (type == 'epsilon') :
                rate.append('0') if zero < one else rate.append('1')
            else:
                print('bad type')
        rowCounter+=1
    return ''.join(rate)

with open('input.txt') as input:
    lines = input.read().splitlines()
    gammaRate = int(calculateRate(lines,'gamma'),2)
    epsilonRate = int(calculateRate(lines,'epsilon'),2)
    print(gammaRate, ' ', epsilonRate)
    powerConsumption = gammaRate * epsilonRate
    print (powerConsumption)



    
        