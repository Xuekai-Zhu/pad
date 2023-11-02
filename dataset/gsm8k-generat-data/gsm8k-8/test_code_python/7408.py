def solution():
    # Define the amounts of rainfall (in inches) in each time period
    rainfall_first_30min = 5
    rainfall_next_30min = rainfall_first_30min / 2
    rainfall_next_hour = 0.5

    # Calculate the total amount of rainfall
    total_rainfall = rainfall_first_30min + rainfall_next_30min + rainfall_next_hour

    # Calculate the average rainfall per hour
    average_rainfall = total_rainfall / 2
    result = average_rainfall
    return result

print(solution())