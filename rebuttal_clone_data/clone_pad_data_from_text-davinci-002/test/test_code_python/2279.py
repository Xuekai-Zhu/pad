def solution():
    minutes_per_session = 30
    sessions_per_day = 2
    days_per_week = 7
    total_hours = minutes_per_session * sessions_per_day * days_per_week / 60
    result = total_hours
    return result

print(solution())