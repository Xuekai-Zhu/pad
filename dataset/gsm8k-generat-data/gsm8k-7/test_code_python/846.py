def solution():
    old_cost_per_day = 0.85
    new_cost_per_day = 0.45
    days_in_month = 30

    # Calculate the total cost for the old refrigerator for the month
    old_total_cost = old_cost_per_day * days_in_month

    # Calculate the total cost for the new refrigerator for the month
    new_total_cost = new_cost_per_day * days_in_month

    # Calculate the amount of money Kurt saves in a month with his new refrigerator
    savings = old_total_cost - new_total_cost
    result = savings
    return result

print(solution())