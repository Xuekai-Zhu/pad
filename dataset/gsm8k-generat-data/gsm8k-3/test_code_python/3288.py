def solution():
    """Flynn watches 30 minutes of tv every night during the weekdays. On the weekends, she watches an additional 2 hours of TV in total. How many hours of tv does she watch in 52 weeks?"""
    # Define the number of minutes Flynn watches TV every weekday
    WEEKDAY_TV_MINUTES = 30

    # Define the number of minutes Flynn watches TV every weekend day
    WEEKEND_TV_MINUTES = 120

    # Calculate the total number of TV minutes in a week
    weekly_tv_minutes = WEEKDAY_TV_MINUTES * 5 + WEEKEND_TV_MINUTES * 2

    # Calculate the total number of TV hours in 52 weeks
    total_tv_hours = weekly_tv_minutes * 52 / 60

    # Display the total number of TV hours
    result = total_tv_hours
    return result

print(solution())