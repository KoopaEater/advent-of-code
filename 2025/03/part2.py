
DIGITS = 12

def find_biggest(line, begin, without):
    slice = line[begin:]
    if without != 0:
        slice = slice[:-without]
    # print("SLICE", slice)
    index = 0
    largest = int(slice[index])
    for i, num_str in enumerate(slice):
        num = int(num_str)
        if num > largest:
            largest = num
            index = i
    # print("LARGEST", largest)
    return index

with open("input.txt", "r") as input:
    sum = 0
    for line in input:
        line = line.strip()
        jolts_str = ""
        last_index = -1
        for without in reversed(range(DIGITS)):
            # print("WITHOUT", without)
            index = find_biggest(line, last_index+1, without)
            index_in_line = last_index + 1 + index
            jolts_str += line[index_in_line]
            last_index = index_in_line
        jolts = int(jolts_str)
        # print("JOLTS", jolts)
        sum += jolts
    print(sum)
