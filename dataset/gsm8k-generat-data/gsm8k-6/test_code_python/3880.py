def solution():
    # Calculate the cost of the previous hay
    prev_cost = 10 * 15  # 10 bales of hay at $15 per bale

    # Calculate the cost of the better quality hay
    better_quality_cost = 20 * 18  # 20 bales of hay (double the delivery) at $18 per bale

    # Calculate the difference in cost
    cost_difference = better_quality_cost - prev_cost

    result = cost_difference
    return result

print(solution())