def solution():
    old_cost = 0.85  # Kurt's old fridge costs $0.85 a day
    new_cost = 0.45  # Kurt's new fridge costs $0.45 a day
    days_per_month = 30  # There are 30 days in a month

    # Calculate how much Kurt saves per day with the new fridge
    savings_per_day = old_cost - new_cost

    # Calculate how much Kurt saves in a 30-day month
    total_savings = savings_per_day * days_per_month
    result = total_savings
    return result

print(solution())