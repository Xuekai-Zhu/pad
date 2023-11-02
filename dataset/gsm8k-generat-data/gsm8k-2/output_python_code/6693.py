def solution():
    """John has started at a job he works every day 10 days ago. So far, he's made $250. How many more days must John work before he makes twice this amount, assuming he makes the same amount every day?"""
    days_worked = 10
    earnings_so_far = 250
    target_earnings = earnings_so_far * 2
    earnings_per_day = earnings_so_far / days_worked
    days_left = (target_earnings - earnings_so_far) / earnings_per_day
    result = days_left
    return result

print(solution())