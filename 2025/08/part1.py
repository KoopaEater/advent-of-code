from functools import reduce

coords = []
with open("input.txt") as input:
    lines = [line.strip().split(",") for line in input.readlines()]
    for line in lines:
        int_line = tuple(map(int, line))
        coords.append(int_line)

dists = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1, z1 = coords[i]
        x2, y2, z2 = coords[j]
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        dist_obj = (dist, [coords[i], coords[j]])
        dists.append(dist_obj)
dists.sort(key=lambda x: x[0])

pair_count = 1000
dists = list(map(lambda x: x[1], dists[:pair_count]))

circuits = []
for pair in dists:
    locs = [None, None]
    for i, box in enumerate(pair):
        for j, circuit in enumerate(circuits):
            if box in circuit:
                locs[i] = j
                break
    match locs:
        case [None, None]:
            circuits.append([pair[0], pair[1]])
        case [i, None]:
            circuits[i].append(pair[1])
        case [None, j]:
            circuits[j].append(pair[0])
        case [i, j]:
            if i == j:
                continue
            circuits[i].extend(circuits[j])
            del circuits[j]

circ_sizes = list(map(len, circuits))
circ_sizes.sort(reverse=True)
circ_size_count = 3
circ_size = circ_sizes[:circ_size_count]

result = reduce(lambda x, y: x * y, circ_size)
print(result)


