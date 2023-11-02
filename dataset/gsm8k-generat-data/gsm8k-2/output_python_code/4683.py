def solution():
    """In the second hour of a storm it rains 7 inches more than twice the amount it rained the first hour. The total amount of rain in the first two hours is 22 inches. How much did it rain in the first hour?"""
    total_rain = 22
    second_hour_rain = 2 * first_hour_rain + 7
    first_hour_rain = (total_rain - second_hour_rain) / 2
    result = first_hour_rain
    return result

print(solution())