def solution():
    # Calculate the total number of slices
    total_slices = 78

    # Calculate the total ratio of slices shared
    total_ratio = 5 + 8

    # Calculate the number of slices Buzz ate
    buzz_slices = 5 * total_slices / total_ratio

    # Calculate the number of slices the waiter ate
    waiter_slices = 8 * total_slices / total_ratio

    # Calculate the result
    result = 20 - waiter_slices
    return result

print(solution())