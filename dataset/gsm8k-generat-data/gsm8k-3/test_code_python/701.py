def solution():
    """Kim buys 3 pizzas. They are 12 slices each. The pizza cost $72. How much did 5 slices cost?"""
    # Define the number of pizzas, slices per pizza, and cost
    pizzas = 3
    slices_per_pizza = 12
    cost = 72

    # Calculate the total number of slices
    total_slices = pizzas * slices_per_pizza

    # Calculate the cost per slice
    cost_per_slice = cost / total_slices

    # Calculate the cost for 5 slices
    cost_5_slices = cost_per_slice * 5

    # Display the cost for 5 slices
    result = cost_5_slices
    return result

print(solution())