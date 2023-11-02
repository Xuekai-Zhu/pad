def solution():
    # Calculate the total cost of the ladders
    cost_50_rungs = 50 * 2  # cost of 50-rung ladders
    cost_60_rungs = 60 * 2  # cost of 60-rung ladders
    total_cost = (10 * cost_50_rungs) + (20 * cost_60_rungs)  # total cost of all ladders
    result = total_cost
    return result

print(solution())