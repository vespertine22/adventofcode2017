#!/usr/bin/python3

with open('input.txt', 'r') as f:
    result = 0
    for line in f:
        a = line.strip().split('\t')
        minimum = int(a[0])
        maximum = int(a[0])
        for i in range(len(a)-1):
            if (int(a[i+1]) > maximum):
                maximum = int(a[i+1])
            if (int(a[i+1]) < minimum):
                minimum = int(a[i+1])
        result += maximum - minimum
    print(result)

# Second task

with open('input.txt', 'r') as f:
    result = 0
    for line in f:
        a = line.strip().split('\t')
        i = 0
        notFound = True
        while notFound and (i < len(a)-1):
            for j in range(i+1, len(a)):
                if (int(a[i]) % int(a[j]) == 0):
                    result += int(a[i]) / int(a[j])
                    notFound = False
                if (int(a[j]) % int(a[i]) == 0):
                    result += int(a[j]) / int(a[i])
                    notFound = False
            i += 1
    print(result)
