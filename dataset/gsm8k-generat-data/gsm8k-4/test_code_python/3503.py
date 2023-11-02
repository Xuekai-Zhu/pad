def solution():
    """It takes Derek 9 minutes to walk a mile if he doesn't have to walk with his brother. If he has to take his brother it takes 12 minutes to walk a mile. How many minutes longer would it take him to walk 20 miles if he had to take his brother?"""
    # Define the time it takes Derek to walk a mile without his brother
    derek_without_brother = 9

    # Define the time it takes Derek to walk a mile with his brother
    derek_with_brother = 12

    # Calculate the time it would take Derek to walk 20 miles without his brother
    time_without_brother = derek_without_brother * 20

    # Calculate the time it would take Derek to walk 20 miles with his brother
    time_with_brother = derek_with_brother * 20

    # Calculate the difference in time
    time_difference = time_with_brother - time_without_brother

    # Return the result
    result = time_difference
    return result

print(solution())