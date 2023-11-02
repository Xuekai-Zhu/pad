def solution():
    # Calculate the cost of the 3 shirts that cost $15 each
    cost_3_shirts = 3 * 15

    # Calculate the number of remaining shirts
    num_remaining_shirts = 5 - 3

    # Calculate the cost of the remaining shirts that cost $20 each
    cost_remaining_shirts = num_remaining_shirts * 20

    # Calculate the total cost of all 5 shirts
    total_cost = cost_3_shirts + cost_remaining_shirts
    result = total_cost
    return result

print(solution())