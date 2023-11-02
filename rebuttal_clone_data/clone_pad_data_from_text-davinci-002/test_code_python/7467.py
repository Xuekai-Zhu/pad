def solution():
    time_without_power = 3
    rate_of_temperature_increase = 8
    target_temperature = 43
    current_temperature = time_without_power * rate_of_temperature_increase + target_temperature
    rate_of_temperature_decrease = 4
    time_to_restore = (current_temperature - target_temperature) / rate_of_temperature_decrease
    result = time_to_restore
    return result

print(solution())