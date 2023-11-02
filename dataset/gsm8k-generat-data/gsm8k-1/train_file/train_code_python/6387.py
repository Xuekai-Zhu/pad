def solution():
    """Tim has some cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys another half the amount of soda cans he had left. If Tim has 24 cans of soda in the end, how many cans of soda did Tim have at first?"""
    cans_at_end = 24
    cans_after_jeff = cans_at_end + 6
    cans_before_half = cans_after_jeff * 2
    total_cans = cans_before_half - 6
    result = total_cans
    return result

print(solution())