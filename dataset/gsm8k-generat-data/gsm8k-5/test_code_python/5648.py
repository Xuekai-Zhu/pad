def solution():
    total_apples = 30  # There are 30 apples in the batch

    # Calculate the number of apples that are either too small or not ripe
    imperfect_apples = (1/6 * total_apples) + (1/3 * total_apples)

    # Calculate the number of perfect apples
    perfect_apples = total_apples - imperfect_apples
    result = perfect_apples
    return result

print(solution())