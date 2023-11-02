def solution():
    total_apples = 30
    small_apples = 1/6 * total_apples
    not_ripe_apples = 1/3 * total_apples

    # Calculate the number of perfect apples
    perfect_apples = total_apples - small_apples - not_ripe_apples
    result = perfect_apples
    return result

print(solution())