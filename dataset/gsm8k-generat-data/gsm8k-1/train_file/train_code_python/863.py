def solution():
    """A coffee shop brews 10 coffee cups per hour on a weekday and 120 coffee cups in total over the weekend. If the coffee shop is open 5 hours a day every single day, how many coffee cups are brewed in 1 week?"""
    weekday_cups_per_hour = 10
    weekend_cups = 120
    weekday_hours_per_day = 5
    days_per_week = 7
    weekday_cups_per_day = weekday_cups_per_hour * weekday_hours_per_day
    total_weekday_cups = weekday_cups_per_day * (days_per_week - 2)
    total_weekend_cups = weekend_cups
    total_cups_per_week = total_weekday_cups + total_weekend_cups
    result = total_cups_per_week
    
    return result

print(solution())