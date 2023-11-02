def solution():
    weekday_sleep = 6 * 5 # 6 hours per day for 5 days per week
    weekend_sleep = 10 * 2 # 10 hours per day for 2 days per week
    total_sleep = weekday_sleep + weekend_sleep
    result = total_sleep
    return result

print(solution())