def solution():
    num_slices = 15
    breakfast_slices = 4
    lunch_slices = 2
    snack_slices = 2
    dinner_slices = 5

    # Calculate the total number of slices Blanch eats
    total_slices_eaten = breakfast_slices + lunch_slices + snack_slices + dinner_slices

    # Calculate the number of slices remaining
    slices_remaining = num_slices - total_slices_eaten
    result = slices_remaining
    return result

print(solution())