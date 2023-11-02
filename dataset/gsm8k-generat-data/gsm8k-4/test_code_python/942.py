def solution():
    """While Paul watches movies, he runs on his treadmill. He can run a mile in 12 minutes. He watches two movies, which are an average length of 1.5 hours. How many miles does he run?"""
    # Define the time taken to run one mile in minutes
    TIME_PER_MILE = 12

    # Define the length of each movie in hours
    MOVIE_LENGTH = 1.5

    # Calculate the total time spent watching movies in minutes
    total_movie_time = MOVIE_LENGTH * 2 * 60

    # Calculate the distance run in miles
    distance = total_movie_time / TIME_PER_MILE

    # return the result
    result = distance
    return result

print(solution())