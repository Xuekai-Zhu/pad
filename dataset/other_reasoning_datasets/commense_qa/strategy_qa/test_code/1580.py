def solution():
    highest_recorded_temp = 108 # in Fahrenheit
    life_threatening_temp = 104 # in Fahrenheit
    if highest_recorded_temp < life_threatening_temp:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())