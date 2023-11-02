def solution():
    mercury_night_temperature = -280
    warm_weather_attire_would_not_protect_in_cold_temperatures = True
    if warm_weather_attire_would_not_protect_in_cold_temperatures and mercury_night_temperature < 0:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())