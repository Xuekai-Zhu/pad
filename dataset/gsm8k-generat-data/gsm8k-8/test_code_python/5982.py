def solution():
    weekday_hours = 4 * 5    # 4 hours a day for 5 days (Monday to Friday)
    weekend_hours = 6 * 2    # 6 hours a day for 2 days (Saturday and Sunday)

    total_hours = weekday_hours + weekend_hours
    result = total_hours
    return result

print(solution())