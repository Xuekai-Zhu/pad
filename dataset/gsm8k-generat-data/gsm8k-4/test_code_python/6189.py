def solution():
    """Four days' temperatures were recorded for Wayupnorth, Canada. The temperatures were: -36 degrees Fahrenheit, +13 degrees Fahrenheit, -15 degrees Fahrenheit, and -10 degrees Fahrenheit. What was the average number of degrees (Fahrenheit) in Wayupnorth, Canada on the 4 days recorded?"""
    # Define the temperatures
    temperatures = [-36, 13, -15, -10]

    # Calculate the sum of the temperatures
    total = sum(temperatures)

    # Calculate the average temperature
    average = total / len(temperatures)

    # Return the result
    result = average
    return result

print(solution())