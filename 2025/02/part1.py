
with open("input.txt", "r") as input:
    line = input.readline()
    search_groups = line.split(',')
    sum = 0
    for group in search_groups:
        nums = group.split('-')
        low = int(nums[0])
        high = int(nums[1])
        for i in range(low, high + 1):
            str_i = str(i)
            len_i = len(str_i)
            if len_i % 2 == 1:
                continue
            mid = len_i // 2
            if str_i[:mid] == str_i[mid:]:
                sum += int(str_i)
    print(sum)