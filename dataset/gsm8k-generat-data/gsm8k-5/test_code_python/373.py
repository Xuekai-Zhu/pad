def solution():
    # Total cost of large tubs
    large_tubs_cost = 3 * 6

    # Total cost of small tubs
    small_tubs_cost = 48 - large_tubs_cost

    # Cost per small tub
    cost_per_small_tub = small_tubs_cost / 6
    result = cost_per_small_tub
    return result

print(solution())