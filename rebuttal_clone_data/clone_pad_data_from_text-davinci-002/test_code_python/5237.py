def solution():
    days_per_week = 5
    weeks = 4
    morning_mile = .5
    afternoon_mile = .5
    total_miles = days_per_week * weeks * (morning_mile + afternoon_mile)
    result = total_miles
    return result

print(solution())