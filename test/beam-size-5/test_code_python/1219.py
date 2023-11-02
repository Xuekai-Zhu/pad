def solution():
    # Calculate the cost of the first 16 minutes of the call
    cost_first_16_min = 0.25 * 16

    # Calculate the cost of the second 16 minutes of the call
    cost_second_16_min = 0.2 * 16

    # Calculate the total cost of the 36-minute call
    total_cost = cost_first_16_min + cost_second_16_min
    result = total_cost
    return result

print(solution())