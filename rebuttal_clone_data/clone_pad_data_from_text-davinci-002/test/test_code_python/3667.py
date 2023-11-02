def solution():
    hourly_rate = 20
    monthly_expenses = 1200
    hours_per_weekday = 3
    hours_per_saturday = 5
    days_per_week = 5
    hours_per_week = hours_per_weekday * days_per_week + hours_per_saturday
    weeks_needed = monthly_expenses / (hourly_rate * hours_per_week)
    result = weeks_needed
    return result

print(solution())