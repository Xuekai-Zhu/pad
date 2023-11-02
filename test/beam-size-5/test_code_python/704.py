def solution():
    days_per_week = 7
    price_per_day = 12
    num_weeks = 2

    # Calculate the total cost of tutoring for one week
    total_cost_per_week = days_per_week * price_per_day

    # Calculate the total cost of tutoring for two weeks
    total_cost = total_cost_per_week * num_weeks
    result = total_cost
    return result

print(solution())