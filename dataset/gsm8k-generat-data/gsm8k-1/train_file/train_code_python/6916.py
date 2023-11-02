def solution():
    """The state of Virginia had 3.79 inches of rain in March, 4.5 inches of rain in April, 3.95 inches of rain in May, 3.09 inches of rain in June and 4.67 inches in July. What is the average rainfall amount, in inches, in Virginia?"""
    total_rainfall = 3.79 + 4.5 + 3.95 + 3.09 + 4.67
    num_months = 5
    average_rainfall = total_rainfall / num_months
    result = average_rainfall
    return result

print(solution())