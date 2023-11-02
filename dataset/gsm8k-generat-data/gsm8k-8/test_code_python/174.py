def solution():
    # Calculate the cost of the tickets
    monday_cost = 5
    wednesday_cost = 2 * monday_cost
    saturday_cost = 5 * monday_cost

    # Calculate the total cost of Glenn's tickets
    total_cost = wednesday_cost + saturday_cost
    result = total_cost
    return result

print(solution())