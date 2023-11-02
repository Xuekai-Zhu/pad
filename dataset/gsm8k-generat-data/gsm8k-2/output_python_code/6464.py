def solution():
    """Thomas is keeping track of the rainfall in May for his science project. On the first day, 26 cm of rain fell. On the second day, 34 cm fell. On the third day, 12 cm less than the second day fell. The average rainfall for the first three days of May is usually 140 cm across all three days, in a normal year. How much less is it raining this year than average?"""
    # Calculate total rainfall for the first three days
    first_day_rainfall = 26
    second_day_rainfall = 34
    third_day_rainfall = second_day_rainfall - 12
    total_rainfall = first_day_rainfall + second_day_rainfall + third_day_rainfall

    # Calculate the difference between this year's rainfall and the average rainfall
    average_rainfall = 140
    difference = average_rainfall - total_rainfall

    return difference

print(solution())