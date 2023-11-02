def solution():
    """How much does it cost you for lunch today at Subway if you pay $40 for a foot-long fish sub and thrice as much for a six-inch cold-cut combo sub?"""
    fish_sub_cost = 40
    cold_cut_cost = 3 * (fish_sub_cost / 2)
    total_cost = fish_sub_cost + cold_cut_cost
    result = total_cost
    return result

print(solution())