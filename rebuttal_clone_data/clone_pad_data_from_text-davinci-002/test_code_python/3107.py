def solution():
    hours_per_week = 20
    weeks_per_month = 4
    total_hours = hours_per_week * weeks_per_month * 2
    sick_hours = hours_per_week
    cathy_hours = total_hours - sick_hours
    result = cathy_hours
    return result

print(solution())