def solution():
    """Ralph watches TV for 4 hours a day from Monday to Friday, and 6 hours a day on Saturday and Sunday. How many hours does Ralph spend watching TV in one week?"""
    # Define the number of hours Ralph watches TV per day on weekdays and weekends
    WEEKDAY_HOURS = 4
    WEEKEND_HOURS = 6

    # Calculate the total number of hours Ralph watches TV in one week
    total_hours = (WEEKDAY_HOURS * 5) + (WEEKEND_HOURS * 2)

    # Display the total number of hours
    result = total_hours
    return result

print(solution())