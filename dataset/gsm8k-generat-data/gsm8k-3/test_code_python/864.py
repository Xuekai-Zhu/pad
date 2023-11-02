def solution():
    """A coffee shop brews 10 coffee cups per hour on a weekday and 120 coffee cups in total over the weekend. 
    If the coffee shop is open 5 hours a day every single day, how many coffee cups are brewed in 1 week?"""
    # Define the number of coffee cups brewed per hour on a weekday
    WEEKDAY_CUPS_PER_HOUR = 10

    # Calculate the number of coffee cups brewed on weekdays
    weekday_cups = WEEKDAY_CUPS_PER_HOUR * 5 * 7

    # Calculate the number of coffee cups brewed on the weekend
    weekend_cups = 120

    # Calculate the total number of coffee cups brewed in a week
    total_cups = weekday_cups + weekend_cups

    # Display the total number of coffee cups brewed in a week
    result = total_cups
    return result

print(solution())