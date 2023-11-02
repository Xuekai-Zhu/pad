def solution():
    """Janna sleeps 7 hours each day during weekdays and 8 hours each day during weekends. How many hours does she sleep in a week?"""
    weekday_hours = 7
    weekend_hours = 8
    total_weekday_hours = weekday_hours * 5
    total_weekend_hours = weekend_hours * 2
    total_hours = total_weekday_hours + total_weekend_hours
    result = total_hours
    return result

print(solution())