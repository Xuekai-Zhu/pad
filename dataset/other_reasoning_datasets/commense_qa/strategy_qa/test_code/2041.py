def solution():
    surface_temperature_Venus = 863
    if surface_temperature_Venus > 98.6: # body temperature in Fahrenheit
        result = "yes"
    else:
        result = "no"
    return result

print(solution())