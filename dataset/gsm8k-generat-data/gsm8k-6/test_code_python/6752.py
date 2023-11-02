def solution():
    # Calculate the total number of apples
    total_apples = 4 * 12  # four dozen apples
    # Calculate the number of apples in each pie
    apples_per_pie = total_apples / 4
    # Calculate the number of apples in each slice of pie
    apples_per_slice = apples_per_pie / 6
    result = apples_per_slice
    return result

print(solution())