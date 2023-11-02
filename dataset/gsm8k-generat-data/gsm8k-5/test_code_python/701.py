def solution():
    total_slices = 3 * 12  # Kim bought 3 pizzas and each pizza has 12 slices
    cost = 72  # Kim spent $72 on the pizzas
    cost_per_slice = cost / total_slices  # Calculate the cost per slice

    # Calculate the cost of 5 slices
    cost_of_five_slices = cost_per_slice * 5
    result = cost_of_five_slices
    return result

print(solution())