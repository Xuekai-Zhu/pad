def solution():
    """Tropical Storm Sally brings 3 days of rain to southern Texas. The first day it rained 4 inches. The second day it rained 5 times as much as the first day, and the third day it rained 6 inches less than the sum of the first two days. How much did it rain on the third day?"""
    # Define the amount of rain on the first day
    day1_rain = 4

    # Define the amount of rain on the second day
    day2_rain = day1_rain * 5

    # Define the amount of rain on the third day
    day3_rain = (day1_rain + day2_rain) - 6

    # Display the amount of rain on the third day
    result = day3_rain
    return result

print(solution())