#/usr/bin/python3


with open('input.txt', 'r') as f:
    for line in f:
        result = 0
        for i in range(len(line)-2):
            if(line[i] == line[i+1]):
                result += int(line[i])

        # wrap around
        if(line.strip()[-1] == line[0]):
            result += int(line[0])

print(result)









