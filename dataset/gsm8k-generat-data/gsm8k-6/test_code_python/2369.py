def solution():
    # Calculate the cost for renting the house for 20 days
    cost_per_day = 50
    cost_14_days = 500
    extra_days = 20 - 14
    cost_extra_days = extra_days * cost_per_day
    total_cost = cost_14_days + cost_extra_days
    result = total_cost
    return result

print(solution())