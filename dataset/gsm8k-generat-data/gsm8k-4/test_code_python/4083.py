def solution():
    """In Hawaii, they normally get an average of 2 inches of rain a day. With 100 days left in the year, they've gotten 430 inches of rain. How many inches on average do they need to finish the year with the normal average?"""
    # Define the normal average rainfall in inches per day
    normal_average = 2

    # Define the number of days left in the year
    days_left = 100

    # Define the total rainfall received so far in inches
    total_rainfall = 430

    # Calculate the average rainfall needed for the rest of the year
    remaining_rainfall = normal_average * days_left - total_rainfall
    average_rainfall_needed = remaining_rainfall / days_left

    # Return the result
    result = average_rainfall_needed
    return result

print(solution())