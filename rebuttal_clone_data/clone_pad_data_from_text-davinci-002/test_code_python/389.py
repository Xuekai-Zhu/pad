def solution():
    rain_1 = 4
    rain_2 = 8
    days = 30
    total_rainfall = rain_1 + rain_2 + ((days - 15) * rain_2)
    result = total_rainfall
    return result

print(solution())