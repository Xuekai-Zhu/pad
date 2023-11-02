def solution():
    """The state of Virginia had 3.79 inches of rain in March, 4.5 inches of rain in April, 3.95 inches of rain in May, 3.09 inches of rain in June and 4.67 inches in July. What is the average rainfall amount, in inches, in Virginia?"""
    # Calculate the total amount of rainfall
    total_rainfall = 3.79 + 4.5 + 3.95 + 3.09 + 4.67

    # Calculate the average rainfall amount
    average_rainfall = total_rainfall / 5

    # return the result
    result = average_rainfall
    return result

print(solution())