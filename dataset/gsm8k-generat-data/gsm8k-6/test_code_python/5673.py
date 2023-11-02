def solution():
    # Calculate the total number of slices eaten by John and Sam
    john_slices = 3
    sam_slices = 2 * john_slices
    total_slices_eaten = john_slices + sam_slices

    # Calculate the number of slices left
    slices_left = 12 - total_slices_eaten
    result = slices_left
    return result

print(solution())