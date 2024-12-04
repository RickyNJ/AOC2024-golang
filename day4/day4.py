find = ["M", "A", "S"]

with open("input.txt", "r") as f:
    arr = [list(line.strip()) for line in f]

result = 0
for h in range(len(arr)):
    for w in range(len(arr[h])):
        if arr[h][w] == "X":
            if h > 2:
                if arr[h-1][w] == find[0] and arr[h-2][w] == find[1] and arr[h-3][w] == find[2]:
                    result += 1

                if w > 2:
                    if arr[h-1][w-1] == find[0] and arr[h-2][w-2] == find[1] and arr[h-3][w-3] == find[2]:
                        result += 1
                if w < len(arr[h])-3:
                    if arr[h-1][w+1] == find[0] and arr[h-2][w+2] == find[1] and arr[h-3][w+3] == find[2]:
                        result += 1
            if h < len(arr)-3:
                if arr[h+1][w] == find[0] and arr[h+2][w] == find[1] and arr[h+3][w] == find[2]:
                    result += 1

                if w > 2:
                    if arr[h+1][w-1] == find[0] and arr[h+2][w-2] == find[1] and arr[h+3][w-3] == find[2]:
                        result += 1
                if w < len(arr[h])-3:
                    if arr[h+1][w+1] == find[0] and arr[h+2][w+2] == find[1] and arr[h+3][w+3] == find[2]:
                        result += 1

            if w > 2:
                if arr[h][w-1] == find[0] and arr[h][w-2] == find[1] and arr[h][w-3] == find[2]:
                    result += 1
            if w < len(arr[h])-3:
                if arr[h][w+1] == find[0] and arr[h][w+2] == find[1] and arr[h][w+3] == find[2]:
                    result += 1
print(result)
