def solution():
    tall_hills = 2
    sleds_down_tall = 4
    small_hills = 3
    sleds_down_small = sleds_down_tall / 2
    total_sleds = (tall_hills * sleds_down_tall) + (small_hills * sleds_down_small)
    result = total_sleds
    return result

print(solution())