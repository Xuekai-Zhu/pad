def solution():
    """In a batch of 30 apples, 1/6 are too small and 1/3 are not ripe. The others are perfect. Calculate the number of perfect apples."""
    total_apples = 30
    small_apples = total_apples / 6
    unripe_apples = total_apples / 3
    perfect_apples = total_apples - small_apples - unripe_apples
    result = perfect_apples
    return result

print(solution())