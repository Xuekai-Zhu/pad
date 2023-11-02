def solution():
    """While Paul watches movies, he runs on his treadmill. He can run a mile in 12 minutes. He watches two movies, which are an average length of 1.5 hours. How many miles does he run?"""
    minutes_per_mile = 12
    movies_watched = 2
    movie_length = 1.5 # in hours
    total_time = movies_watched * movie_length * 60 # in minutes
    total_distance = total_time / minutes_per_mile
    result = total_distance
    return result

print(solution())