def solution():
    # Define cost of meal for Billy and Jenny
    meal_cost = (20 + 5) * 2

    # Calculate total tip
    total_tip = 0.2 * meal_cost

    # Calculate Billy's share of tip
    billy_tip = 0.8 * total_tip / 2

    result = billy_tip
    return result

print(solution())