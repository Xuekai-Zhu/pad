def solution():
    """Based on a 2008 study, children 6–11 years old spend 45 minutes each day watching television.
    How many hours do these children watch television in 2 weeks if they are allowed to watch television 4 days a week?"""
    # Define the number of days and minutes the children watch TV each day
    WATCH_DAYS_PER_WEEK = 4
    WATCH_MINUTES_PER_DAY = 45

    # Calculate the total number of minutes watched in 2 weeks
    total_minutes = WATCH_DAYS_PER_WEEK * WATCH_MINUTES_PER_DAY * 2

    # Convert minutes to hours
    total_hours = total_minutes / 60

    result = total_hours
    return result

print(solution())