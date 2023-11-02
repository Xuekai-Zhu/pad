def solution():
    rain_2pm = 2
    rain_4pm = rain_2pm + (4 * 2)
    rain_7pm = rain_4pm + (3 * 3)
    rain_9pm = rain_7pm + (0.5 * 2)
    total_rain = rain_9pm
    return total_rain

print(solution())