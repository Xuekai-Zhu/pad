def solution():
    """Sherman has a 30-minute commute to the office and a 30-minute commute home every day.  On the weekends, he spends 2 hours, each day, driving his kids to their different activities.  How many hours does Sherman drive a week?"""
    # Define the number of minutes Sherman spends commuting each day
    COMMUTE_MINUTES = 30

    # Define the number of hours Sherman spends driving his kids on weekends
    WEEKEND_HOURS = 4

    # Calculate the total number of hours Sherman drives in a week
    total_hours = (COMMUTE_MINUTES * 2 * 5) / 60 + WEEKEND_HOURS * 2

    # Display the total number of hours
    result = total_hours
    return result

print(solution())