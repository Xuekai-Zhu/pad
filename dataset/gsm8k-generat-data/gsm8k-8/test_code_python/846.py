def solution():
    # Define the cost per day of the old refrigerator
    old_refrigerator_cost = 0.85

    # Define the cost per day of the new refrigerator
    new_refrigerator_cost = 0.45

    # Calculate the difference in cost per day
    cost_savings_per_day = old_refrigerator_cost - new_refrigerator_cost

    # Calculate the cost savings in a 30-day month
    month_savings = cost_savings_per_day * 30

    result = month_savings
    return result

print(solution())