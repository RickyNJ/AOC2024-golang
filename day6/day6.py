with open("input.txt", "r") as f:
    arr = [list(line.strip()) for line in f]

dir = "up"

def findstart(input):
    for i in range(len(input)):
        for c in range(len(input[i])):
            if input[i][c] == "^":
                return i, c

print(findstart(arr))
