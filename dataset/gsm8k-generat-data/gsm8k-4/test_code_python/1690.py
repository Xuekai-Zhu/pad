def solution():
    """On each of 7 Mondays, it rained 1.5 centimeters. On each of 9 Tuesdays it rained 2.5 centimeters. How many more centimeters did it rain on Tuesdays than Mondays?"""
    # Calculate the total amount of rain on Mondays
    mondays_rain = 7 * 1.5

    # Calculate the total amount of rain on Tuesdays
    tuesdays_rain = 9 * 2.5

    # Calculate the difference in the amount of rain on Tuesdays and Mondays
    difference = tuesdays_rain - mondays_rain

    result = difference
    return result

print(solution())