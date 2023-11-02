def solution():
    # Calculate the total number of apple slices
    total_slices = 2 * 8  # 2 apples with 8 slices each

    # Calculate the number of slices given to Jerry
    jerry_slices = (3/8) * total_slices

    # Calculate the number of slices remaining after giving some to Jerry
    remaining_slices = total_slices - jerry_slices

    # Calculate the number of slices Tom ate
    eaten_slices = (1/2) * remaining_slices

    # Calculate the number of slices Tom has left
    slices_left = remaining_slices - eaten_slices
    result = slices_left
    return result

print(solution())