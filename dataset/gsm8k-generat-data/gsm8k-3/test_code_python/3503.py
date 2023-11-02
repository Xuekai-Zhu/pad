def solution():
    """It takes Derek 9 minutes to walk a mile if he doesn't have to walk with his brother. If he has to take his brother it takes 12 minutes to walk a mile. How many minutes longer would it take him to walk 20 miles if he had to take his brother?"""
    # Define the time it takes Derek to walk a mile alone and with his brother
    TIME_ALONE = 9
    TIME_WITH_BROTHER = 12

    # Define the distance Derek needs to walk
    distance = 20

    # Calculate the time it would take Derek to walk the distance alone
    time_alone = TIME_ALONE * distance

    # Calculate the time it would take Derek to walk the distance with his brother
    time_with_brother = TIME_WITH_BROTHER * distance

    # Calculate the difference in time
    time_difference = time_with_brother - time_alone

    # Display the time difference
    result = time_difference
    return result

print(solution())