def solution():
    # Calculate the total number of slices
    total_slices = 2 * 8

    # Calculate the number of slices given to Jerry
    jerry_slices = 3/8 * total_slices

    # Calculate the number of slices remaining after giving some to Jerry
    remaining_slices = total_slices - jerry_slices

    # Calculate the number of slices Tom ate
    eaten_slices = 1/2 * remaining_slices

    # Calculate the number of slices Tom has left
    remaining_slices -= eaten_slices

    result = remaining_slices
    return result

print(solution())