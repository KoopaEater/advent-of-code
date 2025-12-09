
with open("input.txt") as input:
    sections = input.read().split("\n\n")
    fresh_ranges = [tuple(map(int, line.split("-"))) for line in sections[0].split("\n")]
    ingredients = list(map(int, sections[1].split("\n")))
    print(fresh_ranges)
    print(ingredients)
    fresh = 0
    for id in ingredients:
        id = int(id)
        for fresh_range in fresh_ranges:
            low, high = fresh_range
            if low <= id <= high:
                fresh += 1
                break
    print(fresh)