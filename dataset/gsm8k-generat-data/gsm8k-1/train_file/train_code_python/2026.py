def solution():
    """The average temperature in Orlando in a particular week was 60 degrees. If the temperature on each of the first 3 days in that week was 40, and the temperature for Thursday and Friday was 80 degrees each, calculate the total temperature of the remaining days of that week."""
    average_temperature = 60
    temperature_first_three_days = 40
    temperature_thursday = 80
    temperature_friday = 80
    remaining_days = 7 - 3 - 2 # subtracting the number of days for which temperature is given
    total_temperature = (average_temperature * 7) - \
                        (temperature_first_three_days * 3) - \
                        (temperature_thursday + temperature_friday) - \
                        (average_temperature * remaining_days)
    result = total_temperature
    return result

print(solution())