def solution():
    """Kim buys 3 pizzas. They are 12 slices each. The pizza cost $72. How much did 5 slices cost?"""
    # Define the total number of slices
    total_slices = 3 * 12

    # Calculate the cost per slice
    cost_per_slice = 72 / total_slices

    # Calculate the cost of 5 slices
    cost_of_5_slices = cost_per_slice * 5

    # return the result
    result = cost_of_5_slices
    return result

print(solution())