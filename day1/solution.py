#!/usr/bin/python3

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip() # remove \n
        result = result2 = 0
        length = len(line)
        halflength = int(length/2)
        for i in range(length):
            if(line[i] == line[(i+1) % length]):
                result += int(line[i])
            if(line[i] == line[(i + halflength) % length]):
                result2 += int(line[i])

        print('Result #1: ' + str(result) + '\nResult #2: ' + str(result2))
