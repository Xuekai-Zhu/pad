def solution():
    daily_rate = 50.0
    two_weeks_rate = 500.0
    days_in_two_weeks = 14
    extra_days = 20 - days_in_two_weeks

    # Calculate the cost of renting for two weeks
    cost_for_two_weeks = two_weeks_rate

    # Calculate the cost of renting for the extra days
    cost_for_extra_days = extra_days * daily_rate

    # Calculate the total cost of renting for 20 days
    total_cost = cost_for_two_weeks + cost_for_extra_days
    result = total_cost
    return result

print(solution())