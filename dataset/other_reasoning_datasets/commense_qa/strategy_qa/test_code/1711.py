def solution():
    required_temperature = 0 # Celsius
    average_temperature = 27.3 # Celsius
    if average_temperature <= required_temperature:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())