def solution():
    """Three days' temperatures were recorded for Bucyrus, Ohio. The temperatures were -14 degrees Fahrenheit, -8 degrees Fahrenheit, and +1 degree Fahrenheit. What was the average number of degrees (Fahrenheit) in Bucyrus, Ohio on the 3 days recorded?"""
    temps = [-14, -8, 1]
    total_temp = sum(temps)
    average_temp = total_temp / len(temps)
    result = average_temp
    return result

print(solution())