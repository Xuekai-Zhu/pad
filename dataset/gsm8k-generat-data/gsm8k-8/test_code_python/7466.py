def solution():
    # Calculate the cost of clarinet lessons per week
    clarinet_cost_per_week = 40 * 3

    # Calculate the cost of piano lessons per week
    piano_cost_per_week = 28 * 5

    # Calculate the difference in cost per week
    cost_difference_per_week = piano_cost_per_week - clarinet_cost_per_week

    # Calculate the cost difference per year
    cost_difference_per_year = cost_difference_per_week * 52

    result = cost_difference_per_year
    return result

print(solution())