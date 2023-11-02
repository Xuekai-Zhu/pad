def solution():
    total_slices = 12
    john_slices = 3
    sam_slices = 2 * john_slices

    # Calculate the total number of slices eaten
    total_eaten = john_slices + sam_slices

    # Calculate the number of slices left
    slices_left = total_slices - total_eaten
    result = slices_left
    return result

print(solution())