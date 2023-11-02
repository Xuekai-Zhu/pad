def solution():
    """On each of 7 Mondays, it rained 1.5 centimeters. On each of 9 Tuesdays it rained 2.5 centimeters. How many more centimeters did it rain on Tuesdays than Mondays?"""
    # Calculate the total amount of rainfall on Mondays
    monday_rain = 7 * 1.5

    # Calculate the total amount of rainfall on Tuesdays
    tuesday_rain = 9 * 2.5

    # Calculate the difference in rainfall between Tuesdays and Mondays
    difference = tuesday_rain - monday_rain

    # Display the difference in rainfall
    result = difference
    return result

print(solution())