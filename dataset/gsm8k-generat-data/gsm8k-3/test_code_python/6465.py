def solution():
    """Thomas is keeping track of the rainfall in May for his science project. On the first day, 26 cm of rain fell. On the second day, 34 cm fell. On the third day, 12 cm less than the second day fell. The average rainfall for the first three days of May is usually 140 cm across all three days, in a normal year. How much less is it raining this year than average?"""
    # Define the rainfall for the first three days
    rainfall_normal = 140

    # Calculate the rainfall on the third day
    rainfall_3 = 34 - 12

    # Calculate the total rainfall for the first three days
    total_rainfall = 26 + 34 + rainfall_3

    # Calculate the difference between the normal rainfall and the actual rainfall
    difference = rainfall_normal - total_rainfall

    # Display the difference in rainfall
    result = difference
    return result

print(solution())