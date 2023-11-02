def solution():
    total_seeds = 200
    large_planters = 4
    large_planter_size = 20
    small_planters = total_seeds - (large_planters * large_planter_size)
    result = small_planters
    return result

print(solution())