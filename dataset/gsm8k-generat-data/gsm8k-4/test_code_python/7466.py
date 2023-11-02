def solution():
    """Janet pays $40/hour for 3 hours per week of clarinet lessons and $28/hour for 5 hours a week of piano lessons. How much more does she spend on piano lessons than clarinet lessons in a year?"""
    
    # Calculate the cost of clarinet lessons per week and per year
    clarinet_weekly_cost = 40 * 3
    clarinet_yearly_cost = clarinet_weekly_cost * 52

    # Calculate the cost of piano lessons per week and per year
    piano_weekly_cost = 28 * 5
    piano_yearly_cost = piano_weekly_cost * 52

    # Calculate the difference in cost between piano and clarinet lessons
    cost_difference = piano_yearly_cost - clarinet_yearly_cost

    result = cost_difference
    return result

print(solution())