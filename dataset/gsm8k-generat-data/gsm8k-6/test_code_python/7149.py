def solution():
    # Calculate the cost of buying newspapers for one week
    cost_one_week = (0.5 * 3) + 2  # Wednesday, Thursday and Friday newspapers cost $0.5 each, Sunday newspaper costs $2
    # Calculate the total cost of buying newspapers for 8 weeks
    total_cost = cost_one_week * 8
    result = total_cost
    return result

print(solution())