def solution():
    
    tall_hills = 2
    small_hills = 3
    sleds_per_tall_hill = 4
    sleds_per_small_hill = sleds_per_tall_hill / 2
    total_sleds = (tall_hills * sleds_per_tall_hill) + (small_hills * sleds_per_small_hill)
    result = total_sleds
    return result

print(solution())