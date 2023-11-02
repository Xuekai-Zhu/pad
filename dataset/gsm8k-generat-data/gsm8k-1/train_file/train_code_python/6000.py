def solution():
    """Berry is curious about what his average temperature is during the week. On Sunday his temperature is 99.1. On Monday his temperature is 98.2. On Tuesday his temperature is 98.7. On Wednesday his temperature is 99.3. On Thursday his temperature is 99.8. On Friday his temperature is 99. On Saturday his temperature is 98.9. What is his average temperature that week?"""
    temperatures = [99.1, 98.2, 98.7, 99.3, 99.8, 99.0, 98.9]
    total_temperature = sum(temperatures)
    average_temperature = total_temperature / len(temperatures)
    result = average_temperature
    return result

print(solution())