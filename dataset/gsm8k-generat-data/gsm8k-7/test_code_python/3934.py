def solution():
    total_hours = 5
    monday_wednesday_hours = 1.5 * 2  # 1.5 hours on Monday and Wednesday
    tuesday_friday_hours = (total_hours - monday_wednesday_hours) / 2  # Equal time on Tuesday and Friday
    friday_hours = tuesday_friday_hours  # Friday has the same amount of time as Tuesday
    result = friday_hours
    return result

print(solution())