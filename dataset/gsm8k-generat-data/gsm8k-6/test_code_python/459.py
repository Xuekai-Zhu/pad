def solution():
    # Calculate the current cost of one lawnmower
    current_cost = 1800 / (1 - 2/5) # solving for the current cost using the given percentage decrease

    # Calculate the cost of 4 lawnmowers
    total_cost = current_cost * 4

    result = total_cost
    return result

print(solution())