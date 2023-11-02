def solution():
    # Calculate the total number of slices
    total_slices = 2 * 12  # Two large pizzas, each cut into 12 slices

    # Calculate the number of slices left after Dean and his friends have eaten
    hawaiian_slices_left = (0.5 * 12) - 3  # Dean ate half of the Hawaiian pizza, minus the 3 slices Frank ate
    cheese_slices_left = (2/3) * 12  # Sammy ate a third of the cheese pizza, leaving 2/3 of the pizza

    # Add up the remaining slices from both pizzas
    total_slices_left = hawaiian_slices_left + cheese_slices_left
    result = total_slices_left
    return result

print(solution())