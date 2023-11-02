def solution():
    # Calculate the total size of Joyce's new property
    total_size = 2 * 10 + 1  # new property is 10 times larger than previous property, and has a 1-acre pond on it

    # Calculate the size of land suitable for growing vegetables
    vegetable_land = total_size - 1  # subtract the size of the pond

    result = vegetable_land
    return result

print(solution())