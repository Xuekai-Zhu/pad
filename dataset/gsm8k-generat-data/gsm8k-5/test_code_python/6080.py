def solution():
    total_slices = 2 * 12  # There are 2 pizzas, each cut into 12 slices
    slices_eaten = (1/2 + 1/3 + 1/6 + 1/4) * 2 * 12  # Total slices eaten by Bob, Tom, Sally, and Jerry
    slices_left = total_slices - slices_eaten
    result = slices_left
    return result

print(solution())