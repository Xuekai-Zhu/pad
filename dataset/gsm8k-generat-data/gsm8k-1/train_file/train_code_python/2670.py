def solution():
    """Tropical Storm Sally brings 3 days of rain to southern Texas. The first day it rained 4 inches. The second day it rained 5 times as much as the first day, and the third day it rained 6 inches less than the sum of the first two days. How much did it rain on the third day?"""
    day_1_rain = 4
    day_2_rain = day_1_rain * 5
    day_3_rain = (day_1_rain + day_2_rain) - 6
    result = day_3_rain
    return result

print(solution())