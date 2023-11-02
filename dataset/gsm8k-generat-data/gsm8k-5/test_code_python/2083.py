def solution():
    cost_per_can = 10  # James buys pistachios for $10 per can
    ounces_per_can = 5  # Each can contains 5 ounces of pistachios
    ounces_per_week = 30 * 7  # James eats 30 ounces of pistachios every 5 days, so he eats 42 ounces per week

    # Calculate the total cost per week
    cans_per_week = ounces_per_week / ounces_per_can
    cost_per_week = cans_per_week * cost_per_can
    result = cost_per_week
    return result

print(solution())