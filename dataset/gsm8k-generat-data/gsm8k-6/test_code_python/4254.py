def solution():
    # Calculate Tony's temperature above the fever threshold
    normal_temperature = 95
    sickness_temperature_increase = 10
    fever_threshold = 100
    temperature_above_threshold = normal_temperature + sickness_temperature_increase - fever_threshold
    result = temperature_above_threshold
    return result

print(solution())