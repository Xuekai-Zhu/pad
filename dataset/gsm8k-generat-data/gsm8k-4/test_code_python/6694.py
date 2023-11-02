def solution():
    """John has started at a job he works every day 10 days ago. So far, he's made $250. How many more days must John work before he makes twice this amount, assuming he makes the same amount every day?"""
    # Define the number of days John has worked so far and his earnings
    days_worked = 10
    earnings = 250

    # Calculate his earnings per day
    earnings_per_day = earnings / days_worked

    # Calculate the total earnings required to make twice as much as his current earnings
    target_earnings = earnings * 2

    # Calculate the number of additional days needed to reach the target earnings
    additional_days = (target_earnings - earnings) / earnings_per_day

    # return the result rounded up to the nearest whole number
    result = math.ceil(additional_days)
    return result

print(solution())