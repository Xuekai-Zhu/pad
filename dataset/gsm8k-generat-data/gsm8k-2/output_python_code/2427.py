def solution():
    """Wilson decides to go sledding on some nearby hills. On the 2 tall hills, he sleds down them 4 times each and on the 3 small hills, he sled down them half as often as he sleds down the tall hills. How many times did he sled down the hills?"""
    tall_hills = 2
    small_hills = 3
    tall_sleds = 4 * tall_hills
    small_sleds = tall_sleds / 2
    total_sleds = tall_sleds + small_sleds * small_hills
    result = total_sleds
    return result

print(solution())