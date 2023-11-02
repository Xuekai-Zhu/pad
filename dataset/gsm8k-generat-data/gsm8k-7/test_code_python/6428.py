def solution():
    weekdays_swim = (1 + 1) * 5  # 1 hour before and 1 hour after for 5 days a week
    weekend_swim = 3  # 3 hours on the weekend
    total_swim_per_week = weekdays_swim + weekend_swim
    num_weeks = 4
    total_swim = total_swim_per_week * num_weeks
    result = total_swim
    return result

print(solution())