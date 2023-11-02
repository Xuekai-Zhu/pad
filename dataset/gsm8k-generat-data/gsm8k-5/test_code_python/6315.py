def solution():
    tires_cost = 250 * 3  # Jack slashed three tires, each costing $250
    window_cost = 700  # Jack smashed the neighbors' window, costing $700

    # Calculate the total cost of the damages
    total_cost = tires_cost + window_cost
    result = total_cost
    return result

print(solution())