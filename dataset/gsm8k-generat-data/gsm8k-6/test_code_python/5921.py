def solution():
    # Calculate the cost of the call to dad
    cost_dad = 0.05 * 45  # local call costs 5 cents/min

    # Calculate the cost of the call to brother
    cost_brother = 0.25 * 31  # international call costs 25 cents/min

    # Calculate the total cost of the calls
    total_cost = cost_dad + cost_brother
    result = total_cost
    return result

print(solution())