def solution():
    total_slices = 8  # The pizza was cut into 8 slices
    slices_eaten = 3/2 + 3/2  # Angeli and Marlon ate 3/2 slices each

    # Calculate the number of slices left
    slices_left = total_slices - slices_eaten
    result = slices_left
    return result

print(solution())