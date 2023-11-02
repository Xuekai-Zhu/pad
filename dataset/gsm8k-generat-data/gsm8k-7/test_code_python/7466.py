def solution():
    clarinet_rate = 40
    clarinet_hours_per_week = 3
    clarinet_weeks_per_year = 52

    piano_rate = 28
    piano_hours_per_week = 5
    piano_weeks_per_year = 52

    # Calculate the total cost of clarinet lessons per year
    clarinet_cost_per_week = clarinet_rate * clarinet_hours_per_week
    clarinet_cost_per_year = clarinet_cost_per_week * clarinet_weeks_per_year

    # Calculate the total cost of piano lessons per year
    piano_cost_per_week = piano_rate * piano_hours_per_week
    piano_cost_per_year = piano_cost_per_week * piano_weeks_per_year

    # Calculate the difference in cost between piano and clarinet lessons
    cost_difference = piano_cost_per_year - clarinet_cost_per_year
    result = cost_difference
    return result

print(solution())