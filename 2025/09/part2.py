
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

coords = []

with open("input.txt") as input:
    coords = [tuple(map(int, line.strip().split(","))) for line in input.readlines()]

greatest = 0
for i in range(len(coords)):
    x1, y1 = coords[i]
    x2, y2 = coords[(i+1)%len(coords)]
    xa, ya = coords[(i+2)%len(coords)]
    xdir, ydir = sign(x2 - x1), sign(y2 - y1)
    xadir, yadir = sign(xa - x2), sign(ya - y2)
    print((x1, y1), (x2, y2))
    print((xdir, ydir), (xadir, yadir))
    corner1 = None
    corner2 = None
    # Assume the shape is convex
    if xdir != 0:
        if yadir == xdir:
            corner1 = (x1, y1)
            corner2 = (xa, ya)
    elif ydir != 0:
        if xadir != ydir:
            corner1 = (x1, y1)
            corner2 = (xa, ya)
    if corner1 is None:
        continue
    x1, y1 = corner1
    x2, y2 = corner2
    minx, maxx = min(x1, x2), max(x1, x2)
    miny, maxy = min(y1, y2), max(y1, y2)
    for x3, y3 in coords:
        if minx < x3 < maxx and miny < y3 < maxy:
            continue
    area = (maxx - minx) * (maxy - miny)
    if area > greatest:
        greatest = area
print(greatest)
