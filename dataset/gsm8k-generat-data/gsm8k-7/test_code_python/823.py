def solution():
    start_apples = 74
    ricki_removed = 14
    samson_removed = ricki_removed * 2

    # Calculate the total number of apples removed
    total_removed = ricki_removed + samson_removed

    # Calculate the number of apples left in the basket
    num_left = start_apples - total_removed
    result = num_left
    return result

print(solution())