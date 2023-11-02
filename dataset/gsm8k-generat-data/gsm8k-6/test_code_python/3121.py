def solution():
    # Calculate the number of slices left
    total_slices = 8
    slices_eaten = 3/2 + 3/2  # Angeli and Marlon each ate 3/2 slices
    slices_left = total_slices - slices_eaten
    result = slices_left
    return result

print(solution())