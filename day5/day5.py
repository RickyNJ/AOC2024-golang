constraints = {}
result = 0
p2result = 0

def checkagain(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[j] in constraints[input[i]]:
                x = input.pop(j)
                input.insert(i, x)
                return checkagain(input)
    return input[int(len(input)/2)]

def checkarr(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[j] in constraints[input[i]]:
                return 0

    return input[int(len(input)/2)]

with open("input.txt", "r") as f:
    for line in f:
        line = line.split('|')
        if int(line[1]) in constraints:
            constraints[int(line[1])].append(int(line[0]))
        else:
            constraints[int(line[1])] = [int(line[0])]

with open("checks.txt", "r") as f:
    for line in f:
        line = [int(i) for i in line.strip().split(',')]
        lineres = checkarr(line)
        corres = 0
        if lineres == 0:
            corres = checkagain(line)
        result += checkarr(line)
        p2result += corres

print(result)
print(p2result)
