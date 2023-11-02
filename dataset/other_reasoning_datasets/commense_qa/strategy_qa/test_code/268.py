def solution():
    surface_temperature = -200 # assume Europa's surface temperature is around -200 degrees Fahrenheit
    egg_firminess_temperature = 158
    freezing_temperature = 32
    if surface_temperature >= egg_firminess_temperature:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())