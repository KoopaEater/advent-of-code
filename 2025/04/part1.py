
with open("input.txt") as input:
    lines = input.readlines()
    line_len = len(lines[0].strip())
    boogie = []
    boogie.append("0"*(line_len+2))
    for i, line in enumerate(lines):
        line = line.strip().replace("@", "1").replace(".", "0")
        new_line = "0" + line + "0"
        boogie.append(new_line)
    boogie.append("0"*(line_len+2))
    forklift = 0
    for y in range(1, len(lines) + 1):
        for x in range(1, line_len + 1):
            if boogie[y][x] == "0":
                continue
            rolls = 0
            search = [-1, 0, 1]
            for xoff in search:
                for yoff in search:
                    if xoff == 0 and yoff == 0:
                        continue
                    spot = int(boogie[y + yoff][x + xoff])
                    rolls += spot
            if rolls < 4:
                forklift += 1
    print(forklift)