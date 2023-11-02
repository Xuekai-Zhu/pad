def solution():
    """James buys 6 t-shirts for 50% off. They each cost $20. How much did he pay?"""
    # Define the initial cost and the discount
    initial_cost = 20 * 6
    discount = 0.5

    # Calculate the final cost after the discount
    final_cost = initial_cost * (1 - discount)

    # Return the final cost
    result = final_cost
    return result

print(solution())