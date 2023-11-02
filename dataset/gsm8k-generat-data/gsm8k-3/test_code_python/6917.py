def solution():
    """The state of Virginia had 3.79 inches of rain in March, 4.5 inches of rain in April, 3.95 inches of rain in May, 3.09 inches of rain in June and 4.67 inches in July.  What is the average rainfall amount, in inches, in Virginia?"""
    # Define the rainfall amounts for each month
    march_rainfall = 3.79
    april_rainfall = 4.5
    may_rainfall = 3.95
    june_rainfall = 3.09
    july_rainfall = 4.67

    # Calculate the total rainfall for the five months
    total_rainfall = march_rainfall + april_rainfall + may_rainfall + june_rainfall + july_rainfall

    # Calculate the average rainfall per month
    avg_rainfall = total_rainfall / 5

    # Display the average rainfall
    result = avg_rainfall
    return result

print(solution())