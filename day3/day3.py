import re

f = open("input.txt")
result = 0

for line in f:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches =  re.findall(pattern,line)
    for mul in matches:
        mul = re.sub(r"mul[(]", "", mul)
        mul = re.sub(r"[)]", "", mul)
        nums = mul.split(",")
        result += int(nums[0]) * int(nums[1])

print(result)
