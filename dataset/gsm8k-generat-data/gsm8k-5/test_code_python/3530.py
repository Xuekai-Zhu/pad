def solution():
    days_per_week = 5  # Walter works 5 days a week
    hours_per_day = 4  # Walter can only work 4 hours a day
    wage_per_hour = 5  # Walter earns $5 per hour

    # Calculate Walter's weekly earning
    weekly_earning = days_per_week * hours_per_day * wage_per_hour

    # Calculate the amount Walter allocates for his schooling
    school_allocation = weekly_earning * (3/4)
    result = school_allocation
    return result

print(solution())