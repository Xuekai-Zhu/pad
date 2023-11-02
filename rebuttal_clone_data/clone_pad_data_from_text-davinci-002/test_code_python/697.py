def solution():
    hours_per_night = 2
    nights_per_week = 5
    hours_per_day = 3
    days_per_weekend = 2
    weeks_until_exam = 6
    total_hours = hours_per_night * nights_per_week + hours_per_day * days_per_weekend * weeks_until_exam
    result = total_hours
    return result

print(solution())