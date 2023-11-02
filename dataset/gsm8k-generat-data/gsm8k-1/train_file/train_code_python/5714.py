def solution():
    """Three days' temperatures were recorded for Bucyrus, Ohio. The temperatures were -14 degrees Fahrenheit, -8 degrees Fahrenheit, and +1 degree Fahrenheit. What was the average number of degrees (Fahrenheit) in Bucyrus, Ohio on the 3 days recorded?"""
    temp_1 = -14
    temp_2 = -8
    temp_3 = 1
    total_temp = temp_1 + temp_2 + temp_3
    average_temp = total_temp / 3
    result = average_temp
    return result

print(solution())