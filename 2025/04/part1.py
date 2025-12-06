
with open("input_example.txt") as input:
    lines = input.readlines()
    line_len = len(lines[0].strip())
    boogie = []
    boogie.append("0"*(line_len+2))
    for i, line in enumerate(lines):
        line = line.strip().replace("@", "1").replace(".", "0")
        new_line = "0" + line + "0"
        boogie.append(new_line)
    boogie.append("0"*(line_len+2))
    for line in boogie:
        print(line)