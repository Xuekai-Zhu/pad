def solution():
    total_slices = 2 * 12  # total number of slices in 2 pizzas
    slices_eaten = (1/2 + 1/3 + 1/6 + 1/4) * 12  # total number of slices eaten by all 4 people
    slices_left = total_slices - slices_eaten  # total number of slices left over
    result = slices_left
    return result

print(solution())