
pos = 50
maximum = 100
password = 0

with open("input.txt", "r") as input:
    for line in input:
        direction = 1 if line[0] == 'R' else -1
        amount = int(line[1:])
        for i in range(amount):
            pos = (pos + direction) % maximum
            if pos == 0:
                password = password + 1

print(password)
