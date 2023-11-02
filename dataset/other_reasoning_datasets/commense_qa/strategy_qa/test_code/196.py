def solution():
    feb_days = 28
    leap_year = True
    start_day_feb = "Monday"
    if leap_year:
        days_in_feb = feb_days + 1
    else:
        days_in_feb = feb_days
    days_in_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_day_mar = days_in_week[(days_in_week.index(start_day_feb) + days_in_feb) % 7]
    if start_day_mar == start_day_feb:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())