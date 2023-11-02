def solution():
    # Calculate the total cost of the 3 shirts that cost $15 each
    total_cost = 3 * 15

    # Calculate the cost of the remaining two shirts
    remaining_cost = 85 - total_cost

    # Calculate the cost of one of the remaining shirts
    cost_per_shirt = remaining_cost / 2
    result = cost_per_shirt
    return result

print(solution())