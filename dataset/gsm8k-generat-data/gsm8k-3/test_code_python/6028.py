def solution():
    """Bethany loved riding horses.  She rode 1 hour after school every Monday, Wednesday, and Friday.  On Tuesday and Thursday, she rode for 30 min and on Saturdays, she could ride for 2 hours.  How many hours in total did she ride over a 2 week period?"""
    # Calculate the total number of hours ridden in a week
    weekly_hours = (1 + 1 + 1 + 0.5 + 0.5 + 2) # hours per day * number of days

    # Calculate the total number of hours ridden in two weeks
    total_hours = weekly_hours * 2

    # Display the total number of hours ridden
    result = total_hours
    return result

print(solution())