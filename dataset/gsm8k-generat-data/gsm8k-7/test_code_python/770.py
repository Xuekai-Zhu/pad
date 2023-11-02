def solution():
    daily_tv_time = 0.75  # 45 minutes is equivalent to 0.75 hours
    days_per_week = 4
    weeks = 2

    # Calculate the total number of hours spent watching TV
    total_tv_time = daily_tv_time * days_per_week * weeks

    result = total_tv_time
    return result

print(solution())