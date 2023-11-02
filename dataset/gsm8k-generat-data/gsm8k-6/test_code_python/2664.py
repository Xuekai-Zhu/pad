def solution():
    # Calculate the total number of slices in the pizzas
    total_slices = 4 * 12  # 4 pizzas, each with 12 slices
    # Calculate the number of slices left after the guests eat
    slices_left = total_slices - 39
    result = slices_left
    return result

print(solution())