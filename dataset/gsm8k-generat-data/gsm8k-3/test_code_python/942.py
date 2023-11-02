def solution():
    """While Paul watches movies, he runs on his treadmill. He can run a mile in 12 minutes. He watches two movies, which are an average length of 1.5 hours. How many miles does he run?"""
    # Define the time it takes to run a mile and the length of each movie
    MILE_TIME = 12 # minutes
    MOVIE_LENGTH = 1.5 # hours

    # Calculate the total time Paul spends running
    total_time = MOVIE_LENGTH * 2 * 60 # convert hours to minutes and multiply by 2

    # Calculate the number of miles Paul runs
    num_miles = total_time / MILE_TIME

    # Display the number of miles Paul runs
    result = num_miles
    return result

print(solution())