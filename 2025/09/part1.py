
coords = []

with open("input.txt") as input:
    coords = [tuple(map(int, line.strip().split(","))) for line in input.readlines()]

greatest = 0
for x1, y1 in coords:
    for x2, y2 in coords:
        area = (abs(x1 - x2)+1) * (abs(y1 - y2)+1)
        if area > greatest:
            greatest = area
print(greatest)