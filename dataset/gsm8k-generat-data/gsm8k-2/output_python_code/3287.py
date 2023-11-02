def solution():
    """Flynn watches 30 minutes of tv every night during the weekdays. On the weekends, she watches an additional 2 hours of TV in total. How many hours of tv does she watch in 52 weeks?"""
    weekday_minutes = 30 * 5 # 30 minutes per weekday
    weekend_hours = 2 # 2 additional hours on the weekends
    total_weekend_minutes = weekend_hours * 60 # convert additional weekend hours to minutes
    total_minutes_per_week = weekday_minutes + total_weekend_minutes
    total_minutes_per_year = total_minutes_per_week * 52
    total_hours_per_year = total_minutes_per_year / 60
    result = total_hours_per_year
    return result

print(solution())