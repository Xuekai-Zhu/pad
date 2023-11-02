def solution():
    """John has started at a job he works every day 10 days ago. So far, he's made $250. How many more days must John work before he makes twice this amount, assuming he makes the same amount every day?"""
    days_worked = 10
    current_earning = 250
    target_earning = current_earning * 2
    earning_per_day = current_earning / days_worked
    remaining_days = (target_earning - current_earning) / earning_per_day
    result = remaining_days
    return result

print(solution())