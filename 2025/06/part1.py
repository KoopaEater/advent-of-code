from functools import reduce

all_numbers = []
symbols = []

with open("input.txt") as input:
    lines = input.readlines()
    for line in lines[:-1]:
        nums = list(map(int, line.split()))
        all_numbers.append(nums)
    symbols = lines[-1].split()

sum = 0
for i, sym in enumerate(symbols):
    nums = []
    for row in all_numbers:
        nums.append(row[i])
    result = 0
    if sym == "+":
        result = reduce(lambda x, y: x + y, nums)
    elif sym == "*":
        result = reduce(lambda x, y: x * y, nums)
    sum += result
print(sum)