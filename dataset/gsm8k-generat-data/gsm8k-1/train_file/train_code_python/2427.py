def solution():
    """Wilson decides to go sledding on some nearby hills. On the 2 tall hills, he sleds down them 4 times each and on the 3 small hills, he sled down them half as often as he sleds down the tall hills. How many times did he sled down the hills?"""
    tall_hills = 2
    small_hills = 3
    sleds_per_tall_hill = 4
    sleds_per_small_hill = sleds_per_tall_hill / 2
    total_sleds = (tall_hills * sleds_per_tall_hill) + (small_hills * sleds_per_small_hill)
    result = total_sleds
    return result

print(solution())