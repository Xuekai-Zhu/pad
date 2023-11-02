def solution():
    # Calculate the number of apples that are too small and not ripe
    small_apples = 30 * (1/6)
    not_ripe_apples = 30 * (1/3)

    # Calculate the number of perfect apples
    perfect_apples = 30 - small_apples - not_ripe_apples
    result = perfect_apples
    return result

print(solution())