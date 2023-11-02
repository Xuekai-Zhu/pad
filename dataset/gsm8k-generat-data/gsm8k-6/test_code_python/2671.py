def solution():
    # Calculate the total amount of rain over the three days
    total_rain = 4 + 5*4 + (4+5) - 6  # second day it rained 5 times as much, third day it rained 6 inches less than the sum of the first two days
    rain_day_3 = total_rain - (4 + 5)  # third day's rain is the difference between the total and the sum of the first two days
    result = rain_day_3
    return result

print(solution())