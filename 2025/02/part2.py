
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
            for repeat_len in range(1, len_i // 2 + 1):
                if len_i % repeat_len != 0:
                    continue
                repeat_str = str_i[:repeat_len]
                invalid = True
                for j in range(0, len_i, repeat_len):
                    if str_i[j:j+repeat_len] != repeat_str:
                        invalid = False
                        break
                if invalid:
                    sum += int(str_i)
                    break
    print(sum)