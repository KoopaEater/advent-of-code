
lines = []

with open("input.txt") as input:
    lines.extend([list(line.strip().replace(".", "0").replace("S", "1")) for line in input.readlines()])

last_line = lines[0]
for i in range(1, len(lines)):
    last_line = lines[i-1]
    for j, char in enumerate(lines[i]):
        last_char = last_line[j]
        if last_char == "^":
            continue
        if char != "^":
            lines[i][j] = str(int(lines[i][j]) + int(last_char))
        else:
            lines[i][j-1] = str(int(lines[i][j-1]) + int(last_char))
            lines[i][j+1] = str(int(lines[i][j+1]) + int(last_char))

result = 0
for num_str in lines[-1]:
    result += int(num_str)

print(result)