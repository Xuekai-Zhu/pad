def solution():
    # Define the number of slices in a box of pizza
    slices_per_box = 16

    # Calculate the number of slices eaten by the family
    slices_eaten = slices_per_box * 0.75

    # Calculate the number of slices left
    slices_left = slices_per_box - slices_eaten
    result = slices_left
    return result

print(solution())