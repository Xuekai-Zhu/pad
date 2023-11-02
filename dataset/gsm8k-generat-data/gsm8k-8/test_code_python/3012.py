def solution():
    # Calculate the total number of slices needed
    slices_needed = 8 * 2 - 3

    # Calculate the total number of slices from the four cakes
    total_slices = 4 * 6

    # Calculate the number of slices left over
    slices_left_over = total_slices - slices_needed
    result = slices_left_over
    return result

print(solution())