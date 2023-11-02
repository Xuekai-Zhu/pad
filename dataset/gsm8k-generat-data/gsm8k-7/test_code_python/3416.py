def solution():
    temperatures = [40, 50, 65, 36, 82, 72, 26]
    total_temperature = sum(temperatures)
    num_days = len(temperatures)
    average_temperature = total_temperature / num_days
    result = average_temperature
    return result

print(solution())