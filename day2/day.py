f = open("input.txt")

result = 0
def checkDecending(n, firstascend):
    for i in range(1, len(n)):
        if n[i] >= n[i-1] or n[i] - n[i-1] < -3:
            if firstascend:
                c = n.copy()
                del n[i], c [i-1]
                return checkDecending(n, False) or checkDecending(c, False)
            return False
    return True

def checkAcending(n, firstascend):
    for i in range(1, len(n)):
        if n[i] <= n[i-1] or n[i] - n[i-1] > 3:
            if firstascend:
                c = n.copy()
                del n[i], c[i-1]
                return checkAcending(n, False) or checkAcending(c, False)
            return False
    return True

for line in f:
    values = line.split()
    n = []
    for i in range(len(values)):
        n.append(int(values[i]))

    if n[0] > n[-1]:
        if checkDecending(n, True):
            result += 1
    if n[0] < n[-1]:
        if checkAcending(n, True):
            result += 1

print(result)
