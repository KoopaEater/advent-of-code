
with open("input.txt", "r") as input:
    sum = 0
    for line in input:
        line = line.strip()
        index_big = 0
        largest_big = int(line[index_big])
        for i, big_num_str in enumerate(line[:-1]):
            num = int(big_num_str)
            if num > largest_big:
                largest_big = num
                index_big = i
        index_small = index_big + 1
        largest_small = int(line[index_small])
        for j, small_num_str in enumerate(line[index_small:]):
            num = int(small_num_str)
            if num > largest_small:
                largest_small = num
                index_small = index_big + 1 + j
        jolts = int(line[index_big] + line[index_small])
        sum += jolts
    print(sum)