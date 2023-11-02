def solution():
    num_pots = 60
    pots_per_shelf = 15  # 5 pots vertically x 3 sets side-by-side
    num_shelves = num_pots / pots_per_shelf
    result = num_shelves
    return result

print(solution())