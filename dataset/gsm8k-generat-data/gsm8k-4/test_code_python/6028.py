def solution():
    """Bethany loved riding horses. She rode 1 hour after school every Monday, Wednesday, and Friday. On Tuesday and Thursday, she rode for 30 min and on Saturdays, she could ride for 2 hours. How many hours in total did she ride over a 2 week period?"""
    # Calculate the total number of hours Bethany rides during a week
    weekly_hours = (1 * 3) + (0.5 * 2) + 2

    # Calculate the total number of hours Bethany rides during a two week period
    total_hours = weekly_hours * 2

    result = total_hours
    return result

print(solution())