def solution():
    """It rained twice as much on Tuesday as Monday.  On Monday it rained 3 inches more than Sunday.  It rained 4 inches on Sunday.  How much total rainfall was there over the 3 days?"""
    # Define the amount of rain on Sunday
    sun_rain = 4

    # Calculate the amount of rain on Monday
    mon_rain = sun_rain + 3

    # Calculate the amount of rain on Tuesday
    tue_rain = mon_rain * 2

    # Calculate the total amount of rain over the 3 days
    total_rain = sun_rain + mon_rain + tue_rain

    # Display the total amount of rain
    result = total_rain
    return result

print(solution())