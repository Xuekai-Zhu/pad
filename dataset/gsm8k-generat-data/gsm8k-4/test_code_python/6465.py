def solution():
    """Thomas is keeping track of the rainfall in May for his science project. On the first day, 26 cm of rain fell. On the second day, 34 cm fell. On the third day, 12 cm less than the second day fell. The average rainfall for the first three days of May is usually 140 cm across all three days, in a normal year. How much less is it raining this year than average?"""
    # Define the rainfall for each of the first three days in May
    day1 = 26
    day2 = 34
    day3 = day2 - 12

    # Calculate the total rainfall for the first three days of May
    total_rainfall = day1 + day2 + day3

    # Calculate the average rainfall for the first three days of May in a normal year
    average_rainfall = 140

    # Calculate the difference between the actual rainfall and the average rainfall
    difference = average_rainfall - total_rainfall

    # return the result
    result = difference
    return result

print(solution())