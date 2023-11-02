def solution():
    # Calculate the total hours of swimming per week
    daily_swimming = 2
    weekend_swimming = 3
    weekly_swimming = daily_swimming * 5 + weekend_swimming

    # Calculate the total hours of swimming over 4 weeks
    total_swimming = weekly_swimming * 4
    result = total_swimming
    return result

print(solution())