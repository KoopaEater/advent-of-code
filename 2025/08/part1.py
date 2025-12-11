
coords = []
with open("input_example.txt") as input:
    lines = [line.strip().split(",") for line in input.readlines()]
    for line in lines:
        int_line = tuple(map(int, line))
        coords.append(int_line)
print(coords)

dists = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1, z1 = coords[i]
        x2, y2, z2 = coords[j]
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        dist_obj = (dist, (coords[i], coords[j]))
        dists.append(dist_obj)
dists.sort(key=lambda x: x[0])

pair_count = 10
dists = list(map(lambda x: x[1], dists[:pair_count]))
print(dists)

# CONNECT THE CIRCUITS!