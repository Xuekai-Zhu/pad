def solution():
    total_apples = 30
    too_small = total_apples / 6
    not_ripe = total_apples / 3

    # Calculate the number of perfect apples
    perfect_apples = total_apples - too_small - not_ripe
    result = perfect_apples
    return result

print(solution())