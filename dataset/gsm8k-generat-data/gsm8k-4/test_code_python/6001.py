def solution():
    """Berry is curious about what his average temperature is during the week. On Sunday his temperature is 99.1. On Monday his temperature is 98.2. On Tuesday his temperature is 98.7. On Wednesday his temperature is 99.3. On Thursday his temperature is 99.8. On Friday his temperature is 99. On Saturday his temperature is 98.9. What is his average temperature that week?"""
    # Define the temperatures for each day of the week
    sunday_temp = 99.1
    monday_temp = 98.2
    tuesday_temp = 98.7
    wednesday_temp = 99.3
    thursday_temp = 99.8
    friday_temp = 99
    saturday_temp = 98.9

    # Calculate the average temperature for the week
    average_temp = (sunday_temp + monday_temp + tuesday_temp + wednesday_temp + thursday_temp + friday_temp + saturday_temp) / 7

    # Return the average temperature
    result = round(average_temp, 1)
    return result

print(solution())