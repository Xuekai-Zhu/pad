def solution():
    """Flynn watches 30 minutes of tv every night during the weekdays. On the weekends, she watches an additional 2 hours of TV in total. How many hours of tv does she watch in 52 weeks?"""
    minutes_per_weekday = 30 * 5
    minutes_per_weekend = 2 * 60
    minutes_per_week = minutes_per_weekday + minutes_per_weekend
    minutes_per_year = minutes_per_week * 52
    hours_per_year = minutes_per_year / 60
    result = hours_per_year
    return result

print(solution())