def solution():
    first_day_rain = 4
    second_day_rain = 5 * first_day_rain
    third_day_rain = (first_day_rain + second_day_rain) - 6
    result = third_day_rain
    return result

print(solution())