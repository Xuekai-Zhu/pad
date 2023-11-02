def solution():
    sheets_per_week = 60
    days_per_week = 7
    work_days_per_week = 5
    sheets_per_day = sheets_per_week / work_days_per_week
    result = sheets_per_day
    return result

print(solution())