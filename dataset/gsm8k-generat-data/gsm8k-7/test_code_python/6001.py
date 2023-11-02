def solution():
    # Store Berry's temperatures in a list
    temperatures = [99.1, 98.2, 98.7, 99.3, 99.8, 99.0, 98.9]
    
    # Calculate the total temperature by adding all temperatures
    total_temperature = sum(temperatures)
    
    # Calculate the average temperature by dividing the total temperature by the number of days
    average_temperature = total_temperature / len(temperatures)
    
    result = average_temperature
    return result

print(solution())