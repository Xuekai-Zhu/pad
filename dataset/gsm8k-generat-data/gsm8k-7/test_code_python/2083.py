def solution():
    cost_per_can = 10
    ounces_per_can = 5
    ounces_eaten_per_week = 30
    days_per_week = 7

    # Calculate the number of cans of pistachios needed per week
    cans_per_week = ounces_eaten_per_week / ounces_per_can

    # Calculate the cost of pistachios per week
    cost_per_week = cans_per_week * cost_per_can

    result = cost_per_week
    return result

print(solution())