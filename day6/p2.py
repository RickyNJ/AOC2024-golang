from enum import Enum
import time

with open("input.txt", "r") as f:
    arr = [list(line.strip()) for line in f]

def findstart(input):
    for i in range(len(input)):
        for c in range(len(input[i])):
            if input[i][c] == "^":
                return [i, c]
    return []

start = findstart(arr)
x = start[0]
y = start[1]

def peek(coordinates, dir):
    match dir:
        case direction.up:
            if coordinates[0] > 0:
                return arr[coordinates[0]-1][coordinates[1]]
            else:
                return 0

        case direction.right:
            if coordinates[1] < 129:
                return arr[coordinates[0]][coordinates[1]+1]
            else:
                return 0

        case direction.down:
            if coordinates[0] < 129:
                return arr[coordinates[0]+1][coordinates[1]]
            else:
                return 0

        case direction.left:
            if coordinates[1] > 0:
                return arr[coordinates[0]][coordinates[1]-1]
            else:
                return 0

class direction(Enum):
    up = 0
    right = 1
    down = 2
    left = 3

steps = 0
rotations = 0
locations = []

while x >= 0 and x < 130 and y >= 0 and y < 130:
    d = direction(rotations%4)
    next = peek([x, y], d)
    print("current location:", x, y)
    print("facing direction:", d)
    print("next step:", next)
    if next =="." or next == 0 or next == "X":
        if d == direction.up:
            x -= 1
        if d == direction.right:
            y += 1
        if d == direction.down:
            x += 1
        if d == direction.left:
            y -= 1
        if next == ".":
            locations.append([x, y])
            arr[x][y] = "X"
            steps += 1
        if next == 0:
            print("exiting at:", x, y)

    if next == "#":
        rotations += 1
        print("rotating to: ", direction(rotations%4))


def walk(map):
    r, steps, curx, cury = 0, 0, 45, 50
    visitedstates = set()

    while curx >= 0 and curx < 130 and cury >= 0 and cury < 130:
        d = direction(r%4)

        state = (curx, cury, d)
        if state in visitedstates:
            print("loop detected")
            return 1

        visitedstates.add(state)

        next = peek([curx, cury], d)
        if next =="." or next == 0 or next == "X":
            map[curx][cury] = "X"
            if d == direction.up:
                curx -= 1
            if d == direction.right:
                cury += 1
            if d == direction.down:
                curx += 1
            if d == direction.left:
                cury -= 1
            if next == ".":
                steps += 1
            if next == 0:
                print("exiting at:", curx, cury)
                return 0

        if next == "#" or next == "O":
            r += 1

result = 0
for l in locations:
    with open("input.txt", "r") as f:
        arr = [list(line.strip()) for line in f]
    if 0 <= l[0] and l[0] < 130 and 0 <= l[1] and l[1] < 130:
        print("testing: ", l[0], l[1])
        arr[l[0]][l[1]] = "#"
        res = walk(arr)
        if res == 1:
            result += 1
            print("found loop, total: ", result)
        if res == 0:
            print("exit found")
