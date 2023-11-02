def solution():
    water_temperature = 68
    safe_temperature = 40
    if water_temperature > safe_temperature:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())