def solution():
    # Calculate the cost of the Delta Airlines flight after discount
    delta_cost = 850 - (0.2 * 850)

    # Calculate the cost of the United Airlines flight after discount
    united_cost = 1100 - (0.3 * 1100)

    # Find the cheapest flight
    cheapest_cost = min(delta_cost, united_cost)

    # Calculate the amount saved by choosing the cheapest flight
    saved_money = max(delta_cost, united_cost) - cheapest_cost
    result = saved_money
    return result

print(solution())