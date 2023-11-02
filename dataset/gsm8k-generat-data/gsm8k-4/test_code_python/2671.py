def solution():
    """Tropical Storm Sally brings 3 days of rain to southern Texas. The first day it rained 4 inches. The second day it rained 5 times as much as the first day, and the third day it rained 6 inches less than the sum of the first two days. How much did it rain on the third day?"""
    # Define the rainfall on the first and second day
    day1_rainfall = 4
    day2_rainfall = day1_rainfall * 5

    # Calculate the total rainfall on the first two days
    total_rainfall_day1_2 = day1_rainfall + day2_rainfall

    # Calculate the rainfall on the third day
    day3_rainfall = total_rainfall_day1_2 - 6

    result = day3_rainfall
    return result

print(solution())