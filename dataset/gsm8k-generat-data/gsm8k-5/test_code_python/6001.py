def solution():
    # List of Berry's temperatures for the week
    temperatures = [99.1, 98.2, 98.7, 99.3, 99.8, 99, 98.9]

    # Calculate the average temperature
    total_temperature = sum(temperatures)
    average_temperature = total_temperature / len(temperatures)

    result = average_temperature
    return result

print(solution())