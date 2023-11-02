def solution():
    # Calculate the cost for the first 6 months
    cost_first_half = 3 * 6

    # Calculate the cost for the second half, with the doubled rate
    cost_second_half = 6 * 3 * 2

    # Calculate the total cost for the entire year
    total_cost = cost_first_half + cost_second_half

    result = total_cost
    return result

print(solution())