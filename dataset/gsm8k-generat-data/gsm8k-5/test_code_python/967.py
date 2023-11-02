def solution():
    current_temperature = 84  # The current temperature of Addison mountain is 84 degrees
    decrease_factor = 3/4  # The temperature will decrease to 3/4 of its current temperature in one hour

    # Calculate the temperature after one hour
    temperature_after_one_hour = current_temperature * decrease_factor

    # Calculate the temperature decrease
    temperature_decrease = current_temperature - temperature_after_one_hour
    result = temperature_decrease
    return result

print(solution())