def solution():
    """Kim buys 3 pizzas. They are 12 slices each. The pizza cost $72. How much did 5 slices cost?"""
    total_slices = 3 * 12
    total_cost = 72
    cost_per_slice = total_cost / total_slices
    cost_of_5_slices = cost_per_slice * 5
    result = cost_of_5_slices
    return result

print(solution())