
with open("input.txt") as input:
    sections = input.read().split("\n\n")
    fresh_ranges = [list(map(int, line.split("-"))) for line in sections[0].split("\n")]
    fresh_ranges.sort(key=lambda x: x[0])
    new_ranges = [fresh_ranges[0]]
    for next_range in fresh_ranges[1:]:
        high = new_ranges[-1][1]
        if next_range[1] <= high:
            continue
        new_low = max(high+1, next_range[0])
        new_high = next_range[1]
        new_ranges.append([new_low, new_high])
    fresh_ids = 0
    for some_range in new_ranges:
        fresh_ids += some_range[1] - some_range[0] + 1
    print(fresh_ids)
