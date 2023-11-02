def solution():
    """Tropical Storm Sally brings 3 days of rain to southern Texas. The first day it rained 4 inches. The second day it rained 5 times as much as the first day, and the third day it rained 6 inches less than the sum of the first two days. How much did it rain on the third day?"""
    first_day_rain = 4
    second_day_rain = 5 * first_day_rain
    third_day_rain = first_day_rain + second_day_rain - 6
    result = third_day_rain
    return result

print(solution())