def solution():
    hourly_rate = 20
    monthly_expenses = 1200
    weekday_hours = 3 * 5  # 3 hours per day, 5 weekdays
    saturday_hours = 5
    total_hours_weekly = weekday_hours + saturday_hours
    hours_needed_monthly = monthly_expenses / hourly_rate
    weeks_needed = hours_needed_monthly / (total_hours_weekly * 4)  # 4 weeks in a month
    result = weeks_needed
    return result

print(solution())