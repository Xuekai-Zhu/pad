def solution():
    num_slices = 16
    fraction_eaten = 0.75

    # Calculate the number of slices eaten
    num_slices_eaten = num_slices * fraction_eaten

    # Calculate the number of slices left
    num_slices_left = num_slices - num_slices_eaten
    result = num_slices_left
    return result

print(solution())