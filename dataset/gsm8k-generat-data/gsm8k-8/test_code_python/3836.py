def solution():
    # Define the total cost and number of shirts
    total_cost = 85
    num_shirts = 5

    # Calculate the cost of the three shirts that cost $15 each
    cost_15_shirts = 3 * 15

    # Calculate the cost of the remaining two shirts
    cost_remaining_shirts = total_cost - cost_15_shirts

    # Calculate the cost of one remaining shirt
    cost_one_remaining_shirt = cost_remaining_shirts / 2

    result = cost_one_remaining_shirt
    return result

print(solution())