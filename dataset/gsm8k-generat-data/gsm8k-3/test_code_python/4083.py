def solution():
    """In Hawaii, they normally get an average of 2 inches of rain a day. With 100 days left in the year, they've gotten 430 inches of rain. How many inches on average do they need to finish the year with the normal average?"""
    # Define the normal average amount of rain per day
    NORMAL_AVERAGE = 2

    # Get the number of days left in the year
    days_left = 100

    # Calculate the total amount of rain they should have gotten so far this year
    total_expected_rain = NORMAL_AVERAGE * (365 - days_left)

    # Calculate the amount of rain they need to get in the remaining days to reach the normal average
    required_rain = total_expected_rain - 430

    # Calculate the average amount of rain they need per day to reach the normal average
    average_required_rain = required_rain / days_left

    # Display the average amount of rain they need per day
    result = average_required_rain
    return result

print(solution())