with open("input.txt", "r") as f:
    arr = [list(line.strip()) for line in f]
result = 0
for h in range(len(arr)):
    for w in range(len(arr[h])):
        if arr[h][w] == "A" and 0 < w < 139 and 0 < h < 139:
            if (
                (arr[h+1][w+1] == "M" and arr[h-1][w-1] == "S" or arr[h+1][w+1] == "S" and arr[h-1][w-1] == "M") and
                (arr[h+1][w-1] == "M" and arr[h-1][w+1] == "S" or arr[h+1][w-1] == "S" and arr[h-1][w+1] == "M")
            ):
                result += 1
print(result)
