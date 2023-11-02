def solution():
    """Adam needs a new laptop and has two choices. The first laptop is $500, and the second laptop is 3 times as costly as the first laptop. How much would Adam have to spend if he decides to buy both?"""
    # Define the cost of the first laptop and the multiplier for the cost of the second laptop
    LAPTOP_1_COST = 500
    LAPTOP_2_COST_MULTIPLIER = 3

    # Calculate the cost of the second laptop
    laptop_2_cost = LAPTOP_1_COST * LAPTOP_2_COST_MULTIPLIER

    # Calculate the total cost of both laptops
    total_cost = LAPTOP_1_COST + laptop_2_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())