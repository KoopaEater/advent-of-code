from functools import reduce

number_lines = []
symbols = []

with open("input.txt") as input:
    lines = input.readlines()
    number_lines = [line.rstrip("\n") for line in lines[:-1]]
    max_len = 0
    for line in number_lines:
        this_len = len(line)
        if this_len > max_len:
            max_len = this_len
    number_lines = [line.ljust(max_len) for line in number_lines]
    symbol_line = lines[-1].strip()
    for i, sym in enumerate(symbol_line):
        if sym != " ":
            symbols.append((i, sym))

for i, _ in symbols[1:]:
    for j, line in enumerate(number_lines):
        number_lines[j] = line[:i-1] + "|" + line[i:]

numbers_strs = [nums.split("|") for nums in number_lines]
group_count = len(symbols)
groups = [[] for _ in range(group_count)]
for line_strs in numbers_strs:
    for i, num in enumerate(line_strs):
        groups[i].append(num)

sum = 0
for i, group in enumerate(groups):
    len_of_num = len(group[0])
    nums = []
    for j in reversed(range(len_of_num)):
        vert_num_str = ""
        for num_str in group:
            digit = num_str[j]
            if digit == " ":
                continue
            vert_num_str += digit
        nums.append(int(vert_num_str))
    _, sym = symbols[i]
    result = 0
    if sym == "+":
        result = reduce(lambda x, y: x + y, nums)
    elif sym == "*":
        result = reduce(lambda x, y: x * y, nums)
    sum += result
print(sum)