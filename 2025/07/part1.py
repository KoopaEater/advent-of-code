
lines = []
poses = set()

with open("input.txt") as input:
    all_lines = [line.strip() for line in input.readlines()]
    lines.extend(all_lines[1:])
    start_pos = all_lines[0].find("S")
    poses.add(start_pos)

splits = 0
for i, line in enumerate(lines):
    new_poses = set()
    for pos in poses:
        if line[pos] == "^":
            splits += 1
            new_poses.add(pos-1)
            new_poses.add(pos + 1)
        else:
            new_poses.add(pos)
    poses = new_poses

print(splits)