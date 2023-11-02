def solution():
    # Calculate the number of tasks Jerry can complete in a day
    tasks_per_day = 10 // 2  # 5 tasks per day

    # Calculate Jerry's daily earnings
    daily_earnings = tasks_per_day * 40  # $200 per day

    # Calculate Jerry's weekly earnings
    weekly_earnings = daily_earnings * 7  # $1400 per week
    result = weekly_earnings
    return result

print(solution())