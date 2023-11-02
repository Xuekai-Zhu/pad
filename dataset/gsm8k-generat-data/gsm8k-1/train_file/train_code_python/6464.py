def solution():
    """Thomas is keeping track of the rainfall in May for his science project. On the first day, 26 cm of rain fell. On the second day, 34 cm fell. On the third day, 12 cm less than the second day fell. The average rainfall for the first three days of May is usually 140 cm across all three days, in a normal year. How much less is it raining this year than average?"""
    day1_rainfall = 26
    day2_rainfall = 34
    day3_rainfall = day2_rainfall - 12
    total_rainfall = day1_rainfall + day2_rainfall + day3_rainfall
    average_rainfall = 140
    difference = average_rainfall - total_rainfall
    result = difference
    return result

print(solution())