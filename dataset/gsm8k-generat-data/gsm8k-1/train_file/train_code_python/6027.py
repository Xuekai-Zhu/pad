def solution():
    """Bethany loved riding horses. She rode 1 hour after school every Monday, Wednesday, and Friday. On Tuesday and Thursday, she rode for 30 min and on Saturdays, she could ride for 2 hours. How many hours in total did she ride over a 2 week period?"""
    days_per_week = 7
    weeks = 2
    monday_wednesday_friday_hours = 1 * 3
    tuesday_thursday_hours = 0.5 * 2
    saturday_hours = 2
    total_hours = (monday_wednesday_friday_hours + tuesday_thursday_hours + saturday_hours) * days_per_week * weeks
    result = total_hours
    return result

print(solution())