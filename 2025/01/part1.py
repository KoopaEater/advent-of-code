
pos = 50
password = 0

with open("input.txt", "r") as input:
    for line in input:
        dir = 1 if line[0] == 'R' else -1
        amount = int(line[1:])
        pos = (pos + dir * amount) % 100
        if pos == 0:
            password = password + 1

print(password)