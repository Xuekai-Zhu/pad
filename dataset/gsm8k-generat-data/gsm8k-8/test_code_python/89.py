def solution():
    daily_average = 40
    friday_average = daily_average * 1.4
    weekly_total = (daily_average * 4) + friday_average
    result = weekly_total
    return result

print(solution())