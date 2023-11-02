def solution():
    tasks_per_day = 100  # Tim does 100 tasks per day
    pay_per_task = 1.2  # Each task pays $1.2
    days_per_week = 6  # Tim works 6 days per week

    # Calculate Tim's weekly earnings
    weekly_earnings = tasks_per_day * pay_per_task * days_per_week

    result = weekly_earnings
    return result

print(solution())