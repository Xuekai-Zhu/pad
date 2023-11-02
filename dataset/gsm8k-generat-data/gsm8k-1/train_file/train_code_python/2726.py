def solution():
    """Oshea bought 200 basil seeds. He wants to plant them in planters. He has 4 large planters that can hold 20 seeds each. He also has small planters that can hold 4 seeds each. How many small planters will he need to plant all the basil seeds?"""
    large_planter_capacity = 20
    small_planter_capacity = 4
    large_planters_needed = 200 // large_planter_capacity
    small_seeds_needed = 200 % large_planter_capacity
    small_planters_needed = (small_seeds_needed + (small_planter_capacity - 1)) // small_planter_capacity
    total_planters_needed = large_planters_needed + small_planters_needed
    result = small_planters_needed
    return result

print(solution())