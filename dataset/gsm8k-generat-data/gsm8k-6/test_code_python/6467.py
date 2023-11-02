def solution():
    temperature_NY = 80  # temperature in New York in June 2020
    temperature_Miami = temperature_NY + 10  # temperature in Miami is 10 degrees hotter than in New York
    temperature_SD = temperature_Miami + 25  # temperature in San Diego is 25 degrees cooler than in Miami
    average_temperature = (temperature_NY + temperature_Miami + temperature_SD) / 3  # calculate the average temperature
    result = average_temperature
    return result

print(solution())