def solution():
    """Janna sleeps 7 hours each day during weekdays and 8 hours each day during weekends. How many hours does she sleep in a week?"""
    weekday_hours = 7
    weekend_hours = 8
    days_weekday = 5
    days_weekend = 2
    total_hours = (weekday_hours * days_weekday) + (weekend_hours * days_weekend)
    result = total_hours
    return result

print(solution())