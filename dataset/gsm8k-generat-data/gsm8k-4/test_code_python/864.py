def solution():
    """A coffee shop brews 10 coffee cups per hour on a weekday and 120 coffee cups in total over the weekend. If the coffee shop is open 5 hours a day every single day, how many coffee cups are brewed in 1 week?"""
    # Define the number of coffee cups brewed during the weekdays
    weekday_coffee_cups = 10 * 5 * 5  # 10 cups per hour, 5 hours per day, 5 weekdays in a week

    # Define the number of coffee cups brewed over the weekend
    weekend_coffee_cups = 120

    # Calculate the total number of coffee cups brewed in a week
    total_coffee_cups = weekday_coffee_cups + weekend_coffee_cups

    result = total_coffee_cups
    return result

print(solution())