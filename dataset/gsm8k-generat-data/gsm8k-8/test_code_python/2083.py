def solution():
    # Calculate how many cans James eats every 5 days
    cans_per_5_days = 30 / 5 / 5

    # Calculate how much James spends on pistachios per can
    cost_per_can = 10

    # Calculate how much James spends on pistachios per week
    cost_per_week = cans_per_5_days * cost_per_can * 7
    result = cost_per_week
    return result

print(solution())