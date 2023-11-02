def solution():
    """Tim has some cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys another half the amount of soda cans he had left. If Tim has 24 cans of soda in the end, how many cans of soda did Tim have at first?"""
    cans_left_after_jeff = 0
    total_cans = 0
    jeff_cans = 6
    final_cans = 24
    for i in range(final_cans):
        if i == jeff_cans:
            cans_left_after_jeff = total_cans
        if i == cans_left_after_jeff + (cans_left_after_jeff/2):
            total_cans += cans_left_after_jeff/2
        total_cans += 1
    result = total_cans
    return result

print(solution())