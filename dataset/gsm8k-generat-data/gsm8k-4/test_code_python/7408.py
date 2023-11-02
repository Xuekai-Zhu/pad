def solution():
    """A storm dropped 5 inches of rain in the first thirty minutes. In the next 30 minutes, the hurricane dropped half that amount of rain. It then dropped 1/2 inch of rain for the next hour. What was the average rainfall total for the duration of the storm?"""
    # Define the rainfall measurements
    rainfall_first_30 = 5
    rainfall_second_30 = 0.5 * rainfall_first_30
    rainfall_next_60 = 0.5

    # Calculate the total rainfall
    total_rainfall = rainfall_first_30 + rainfall_second_30 + rainfall_next_60

    # Calculate the average rainfall
    average_rainfall = total_rainfall / 2

    # Return the result
    result = average_rainfall
    return result

print(solution())