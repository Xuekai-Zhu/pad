def solution():
    initial_liters = 6000
    evaporated_liters = 2000
    drained_liters = 3500
    minutes_of_rain = 30
    rain_interval = 10
    rain_liters_per_interval = 350
    rain_liters = minutes_of_rain / rain_interval * rain_liters_per_interval
    final_liters = initial_liters + rain_liters - evaporated_liters - drained_liters
    result = final_liters
    return result

print(solution())