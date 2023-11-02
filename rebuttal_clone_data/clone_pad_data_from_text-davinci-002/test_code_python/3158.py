def solution():
    hours_needed = 40
    hours_per_session = 2
    sessions_per_week = 2
    weeks_needed = hours_needed / (hours_per_session * sessions_per_week)
    result = weeks_needed
    return result

print(solution())